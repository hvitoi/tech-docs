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
     * Consumer id
     * this is an arbitrary name for the consumer used for logging on the server
     * be default it uses consumer-<groupname>-<randomnumber>
     */
    configs.setProperty(ConsumerConfig.CLIENT_ID_CONFIG, "awesome-consumer");

    /**
     * Consumer group
     */
    configs.setProperty(ConsumerConfig.GROUP_ID_CONFIG, "my-group");

    /**
     * Class to serialize the key
     */
    configs.setProperty(ConsumerConfig.KEY_DESERIALIZER_CLASS_CONFIG, StringDeserializer.class.getName());

    /**
     * Class to serialize the value
     */
    configs.setProperty(ConsumerConfig.VALUE_DESERIALIZER_CLASS_CONFIG, StringDeserializer.class.getName());

    /**
     * What to do when there is no initial offset in Kafka or if the current offset
     * does not exist any more on the server (e.g. because that data has been
     * deleted)
     * 
     * For example, when a new consumer group is created, it has no committed
     * offsets yet. Thus is must define where to start consuming
     * 
     * "earliest": automatically reset the offset to the earliest offset (offset 0)
     * "latest": automatically reset the offset to the latest offset
     * "none": throw exception to the consumer if no previous offset is found for
     * the consumer's group
     */
    configs.setProperty(ConsumerConfig.AUTO_OFFSET_RESET_CONFIG, "earliest");

    /**
     * Maximum numbers of records to fetch per poll.
     * When this number is reached, the poll is closed (even there is still time)
     * 
     * Increase it if the messages are small in size and your RAM is huge.
     * It's good practice to monitor how many records are being
     * polled per request
     * 
     * After the poll is complete (by time or by messages), the records are
     * committed (if auto commit is enabled)
     * 
     * Defaults to 500 messages.
     */
    configs.setProperty(ConsumerConfig.MAX_POLL_RECORDS_CONFIG, "5");

    /**
     * Automatically commit offset or not
     * 
     * if disabled, the code must manually commit the message
     */
    configs.setProperty(ConsumerConfig.ENABLE_AUTO_COMMIT_CONFIG, "true");

    /**
     * Defines the commit interval, if enable.auto.commit=true.
     * Defaults to 5s
     */
    configs.setProperty(ConsumerConfig.AUTO_COMMIT_INTERVAL_MS_CONFIG, "5");

  }
}
