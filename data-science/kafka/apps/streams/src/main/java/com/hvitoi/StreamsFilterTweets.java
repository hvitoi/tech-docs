package com.hvitoi;

import java.util.Properties;

import com.google.gson.JsonParser;
import org.apache.kafka.common.serialization.Serdes;
import org.apache.kafka.streams.KafkaStreams;
import org.apache.kafka.streams.StreamsBuilder;
import org.apache.kafka.streams.StreamsConfig;
import org.apache.kafka.streams.kstream.KStream;

public class StreamsFilterTweets {
  public static void main(String[] args) {
    // properties
    Properties properties = new Properties();
    properties.setProperty(StreamsConfig.BOOTSTRAP_SERVERS_CONFIG, "localhost:9092");
    properties.setProperty(StreamsConfig.APPLICATION_ID_CONFIG, "demo-kafka-streams"); // similar to consumer group
    properties.setProperty(StreamsConfig.DEFAULT_KEY_SERDE_CLASS_CONFIG, Serdes.StringSerde.class.getName()); // key
                                                                                                              // serializer
    properties.setProperty(StreamsConfig.DEFAULT_VALUE_SERDE_CLASS_CONFIG, Serdes.StringSerde.class.getName()); // value
                                                                                                                // serializer

    // create topology
    StreamsBuilder streamsBuilder = new StreamsBuilder();

    // input topic
    KStream<String, String> inputTopic = streamsBuilder.stream("tweets");
    // filter tweets with user that has 10000+// followers
    KStream<String, String> filteredStream = inputTopic
        .filter((key, value) -> extractUserFollowersInTweet(value) > 10000);
    filteredStream.to("important_tweets"); // output topic

    // build the topology
    KafkaStreams kafkaStreams = new KafkaStreams(streamsBuilder.build(), properties);

    // start our streams application
    kafkaStreams.start();
  }

  private static JsonParser jsonParser = new JsonParser();

  private static Integer extractUserFollowersInTweet(String tweetJson) {
    try {
      return jsonParser.parse(tweetJson).getAsJsonObject().get("user").getAsJsonObject().get("followers_count")
          .getAsInt();
    } catch (NullPointerException e) {
      return 0;
    }
  }

}
