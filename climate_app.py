# -*- coding: utf-8 -*-
"""
Created on Fri Jul 17 09:17:13 2020

@author: betsy_k
"""

import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
import datetime as dt

from flask import Flask, jsonify


#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///Resources/hawaii.sqlite")

Base = automap_base()
Base.prepare(engine, reflect=True)

Measurement = Base.classes.measurement
Station = Base.classes.station

#################################################
# Flask Setup
#################################################
app = Flask(__name__)


query_date = dt.date(2017, 8, 23) - dt.timedelta(days=365)

#################################################
# Flask Routes
#################################################

@app.route("/")
def welcome():
    """List all available api routes."""
    return (
        f"Welcome to the Climate App<br/>"
        f"--------------------------------------<br/>"
        f"Available Routes:<br/>"
        f" <br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/<start><br/>"
        f"    (Enter  a start date with form: YYYY-MM-DD<br/>"
        f"/api/v1.0/<start>/<end><br/>"   
        f"    (Enter a start date and an end date with form: YYYY-MM-DD"
    )


@app.route("/api/v1.0/precipitation")
def precip():
    session = Session(engine)  
    
    results = session.query(Measurement.date, Measurement.prcp).filter(Measurement.date >= query_date).\
    order_by(Measurement.date).all()
    
    session.close()
    
    precip_by_date = []
    for date, prcp in results:
        pd_dict = {}
        pd_dict["Date"] = date
        pd_dict["Precipitation"] = prcp
        precip_by_date.append(pd_dict)
        
    return jsonify(precip_by_date)


@app.route("/api/v1.0/stations")
def stations():
    session = Session(engine)
    
    results = session.query(Station.station, Station.name).all()
    
    session.close()
    
    station_list = []
    for station, name in results:
        st_dict = {}
        st_dict["Station"] = station
        st_dict["Name"] = name
        station_list.append(st_dict)
        
    return jsonify(station_list)    


@app.route("/api/v1.0/tobs")
def temps():
    session = Session(engine)
    
    results = session.query(Measurement.date, Measurement.tobs).filter(Measurement.date >= query_date).\
    filter(Measurement.station == 'USC00519281').all()

    session.close()
    
    temp_by_date = []
    for date, tobs in results:
        tob_dict = {}
        tob_dict["Date"] = date
        tob_dict["Temperature"] = tobs
        temp_by_date.append(tob_dict)
        
    return jsonify(temp_by_date)  


@app.route("/api/v1.0/<start_date>")
def stats_st(start_date):
    if start_date >= "2010-01-01" and start_date <= "2017-08-23":
        session = Session(engine)
    
        sel = [func.min(Measurement.tobs), func.max(Measurement.tobs), func.avg(Measurement.tobs)]
    
        results = session.query(*sel).filter(Measurement.date >= start_date).all()
    
        session.close()

        stats = list(np.ravel(results))
        min_temp = stats[0]
        max_temp = stats[1]
        avg_temp = round(stats[2],1)
    
        st_dict = {
            "Min Temp": min_temp,
            "Max Temp": max_temp,
            "Avg Temp": avg_temp
            }
        
        return jsonify(st_dict)
    
    else:
        return jsonify({"error": f"Date not in range, must be between 2010-01-01 and 2017-08-23."}), 404
    
    
@app.route("/api/v1.0/<start_date>/<end_date>")
def stats_se(start_date, end_date):
    if (start_date >= "2010-01-01" and start_date <= "2017-08-23") and (end_date >= "2010-01-01" and end_date <= "2017-08-23"):
        session = Session(engine)
    
        sel = [func.min(Measurement.tobs), func.max(Measurement.tobs), func.avg(Measurement.tobs)]
    
        results = session.query(*sel).filter(Measurement.date >= start_date, Measurement.date <= end_date).all()
    
        session.close()
    
        stats = list(np.ravel(results))
        min_temp = stats[0]
        max_temp = stats[1]
        avg_temp = round(stats[2],1)
    
        st_dict = {
            "Min Temp": min_temp,
            "Max Temp": max_temp,
            "Avg Temp": avg_temp
            }
        
        return jsonify(st_dict)    
           
    else:
        return jsonify({"error": f"Date not in range, must be between 2010-01-01 and 2017-08-23."}), 404
    


if __name__ == "__main__":
    app.run(debug=True)