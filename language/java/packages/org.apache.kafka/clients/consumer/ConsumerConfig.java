import java.util.Properties;

import org.apache.kafka.clients.consumer.ConsumerConfig;
import org.apache.kafka.common.serialization.StringDeserializer;

class Main {
  public static void main(String[] args) {
    Properties configs = new Properties();

    /**
     * kafka broker to consume from
     */
    configs.setProperty(ConsumerConfig.BOOTSTRAP_SERVERS_CONFIG, "localhost:9092");

    /**
     * Class to serialize the key
     */
    configs.setProperty(ConsumerConfig.KEY_DESERIALIZER_CLASS_CONFIG, StringDeserializer.class.getName());

    /**
     * Class to serialize the value
     */
    configs.setProperty(ConsumerConfig.VALUE_DESERIALIZER_CLASS_CONFIG, StringDeserializer.class.getName());

    /**
     * Consumer group
     */
    configs.setProperty(ConsumerConfig.GROUP_ID_CONFIG, "my-group");

    /**
     * earliest: very beginning
     * latest: new messages
     * none: none
     */
    configs.setProperty(ConsumerConfig.AUTO_OFFSET_RESET_CONFIG, "earliest");

  }
}
