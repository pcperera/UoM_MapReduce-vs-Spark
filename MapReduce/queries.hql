SELECT Year, avg((CarrierDelay /ArrDelay)*100) from DelayedFlights GROUP BY Year;
SELECT Year, avg((NASDelay /ArrDelay)*100) from DelayedFlights GROUP BY Year;
SELECT Year, avg((WeatherDelay /ArrDelay)*100) from DelayedFlights GROUP BY Year;
SELECT Year, avg((LateAircraftDelay /ArrDelay)*100) from DelayedFlights GROUP BY Year;
SELECT Year, avg((SecurityDelay /ArrDelay)*100) from DelayedFlights GROUP BY Year;