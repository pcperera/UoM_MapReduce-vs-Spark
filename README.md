<!-- TOC -->
    * [Introduction](#introduction)
    * [Analysis](#analysis)
      * [MapReduce](#mapreduce)
      * [Spark](#spark)
    * [Evaluation](#evaluation)
        * [Heterogeneous query evaluation](#heterogeneous-query-evaluation)
        * [Homogeneous query evaluation](#homogeneous-query-evaluation)
          * [Average comparison](#average-comparison)
    * [Conclusion](#conclusion)
<!-- TOC -->


### Introduction

Evaluation of MapReduce and Spark for the given dataset and queries is summarized in this README file. Below directories contain raw data, log output, images and recordings.

* MapReduce - MapReduce raw data
* Spark - Spark raw data
* data - raw data
* evaluation - MapReduce and Spark analysis raw data and recordings.


### Analysis

#### MapReduce

![cluster.png](MapReduce%2Fcluster.png)

1. ssh -i "~/vockey.pem" hadoop@ec2-3-88-33-238.compute-1.amazonaws.com
2. scp -i "~/vockey.pem" data/DelayedFlights-updated.csv hadoop@ec2-3-88-33-238.compute-1.amazonaws.com:~/
3. scp -i "~/vockey.pem" MapReduce/*.hql MapReduce/*.sh hadoop@ec2-3-88-33-238.compute-1.amazonaws.com:~/
4. hadoop fs -mkdir /flights
5. hadoop fs -put DelayedFlights-updated.csv /flights/
6. hive
7. source load-delayed-flights.hql;
8. chmod +x run-queries.sh
9. ./run-queries.sh > run-queries.log

#### Spark

![cluster.png](Spark%2Fcluster.png)

1. ssh -i ~/vockey.pem hadoop@ec2-34-239-248-169.compute-1.amazonaws.com
2. scp -i "~/vockey.pem" Spark/*.py hadoop@ec2-34-239-248-169.compute-1.amazonaws.com:~/
3. spark-submit load-and-process.py


### Evaluation

![results.png](MapReduce%2Fresults.png)
![results.png](Spark%2Fresults.png) 

##### Heterogeneous query evaluation
![Heterogeneous batch runtime vs Iteration.png](evaluation%2FHeterogeneous%20batch%20runtime%20vs%20Iteration.png)
![(MapReduce over Spark)  Heterogeneous Query Runtime Ratio.png](evaluation%2F%28MapReduce%20over%20Spark%29%20%20Heterogeneous%20Query%20Runtime%20Ratio.png)

##### Homogeneous query evaluation
![Homogeneous query total runtime in 5 iterations.png](evaluation%2FHomogeneous%20query%20total%20runtime%20in%205%20iterations.png)
![(MapReduce over Spark)  Homegeneous Query Runtime Ratio.png](evaluation%2F%28MapReduce%20over%20Spark%29%20%20Homegeneous%20Query%20Runtime%20Ratio.png)

###### Average comparison 
![Homogeneous query average runtime.png](evaluation%2FHomogeneous%20query%20average%20runtime.png)
![(MapReduce over Spark) Homegeneous Query Average Exeuction Time Ratio.png](evaluation%2F%28MapReduce%20over%20Spark%29%20Homegeneous%20Query%20Average%20Exeuction%20Time%20Ratio.png)

### Conclusion

1. Spark is significantly faster than MapReduce for the processing of given data set.
2. Spark is relatively easy to use for data loading and execution because of more high level API support such as Python and Scala.
3. MapReduce in contrast relatively less easy to use because of the less declarative API support which involved writing more lines of code. 