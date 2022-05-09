import java.time.Duration;
import java.util.Collections;
import java.util.Properties;

import org.apache.kafka.clients.consumer.ConsumerConfig;
import org.apache.kafka.clients.consumer.ConsumerRecords;
import org.apache.kafka.clients.consumer.KafkaConsumer;
import org.apache.kafka.common.serialization.StringSerializer;

class Main {
  public static void main(String[] args) {
    /**
     * Static
     */
    ConsumerRecordsNew.run();

    /**
     * Instance
     */

  }

}

class ConsumerRecordsNew {
  static ConsumerRecords<String, String> run() {
    Properties configs = new Properties();
    configs.setProperty(ConsumerConfig.BOOTSTRAP_SERVERS_CONFIG, "localhost:9092");
    configs.setProperty(ConsumerConfig.KEY_DESERIALIZER_CLASS_CONFIG, StringSerializer.class.getName());
    configs.setProperty(ConsumerConfig.VALUE_DESERIALIZER_CLASS_CONFIG, StringSerializer.class.getName());

    KafkaConsumer<String, String> consumer = new KafkaConsumer<>(configs);

    consumer.subscribe(Collections.singletonList("my-topic"));

    ConsumerRecords<String, String> records = consumer.poll(Duration.ofMillis(100));

    return records;
  }

}
