IST3134 – MapReduce Word Count Project
This repository contains the group assignment for IST3134 Big Data Analytics.
The project demonstrates MapReduce processing on a large Wikipedia/Wikidata dataset to perform word frequency analysis.

Dataset
We used a Wikidata XML dump, which is publicly available:

Download Link:
https://dumps.wikimedia.org/wikidatawiki/20250420/wikidatawiki-20250420-pages-articles-multistream7.xml-p7552572p7838096.bz2

Type: Unstructured XML

Size: ~4GB uncompressed

Content: Articles and metadata for Wikidata pages

PyStream/ → Python MapReduce using Hadoop Streaming

Sample outputs → Top word counts from both implementations

How to Run
Python MapReduce (Hadoop Streaming)
bash
hadoop jar /usr/lib/hadoop-mapreduce/hadoop-streaming.jar \
    -input /wikidata/wikidata.xml \
    -output /wikidata/output_python \
    -mapper mapper.py \
    -reducer reducer.py
Java MapReduce (Native Hadoop)
Compile and package into a JAR:

bash
javac -classpath `hadoop classpath` -d . WordCountMapper.java WordCountReducer.java WordCountDriver.java
jar -cvf mywordcount.jar *.class
Run in Hadoop:

bash
hadoop jar mywordcount.jar WordCountDriver /wikidata/wikidata.xml /wikidata/output_java