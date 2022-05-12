import java.util.Properties;
import org.apache.kafka.clients.producer.ProducerConfig;
import org.apache.kafka.common.serialization.StringSerializer;

class Main {
  public static void main(String[] args) {
    Properties configs = new Properties();

    /**
     * kafka broker to produce to
     */
    configs.setProperty(ProducerConfig.BOOTSTRAP_SERVERS_CONFIG, "localhost:9092");

    /**
     * Class to serialize the key
     */
    configs.setProperty(ProducerConfig.KEY_SERIALIZER_CLASS_CONFIG, StringSerializer.class.getName());

    /**
     * Class to serialize the value
     */
    configs.setProperty(ProducerConfig.VALUE_SERIALIZER_CLASS_CONFIG, StringSerializer.class.getName());

    /**
     * Idempotent producer
     * Automatically sets
     * - acks=all
     * - retries=infinity
     * - max.in.flight.requests: 5 (but guarantees the ordering!)
     */
    configs.setProperty(ProducerConfig.ENABLE_IDEMPOTENCE_CONFIG, "true");

    /**
     * acks=0: producer won't wait for ack (possible data loss) - dangerous!
     * acks=1: producer wait for leader ack (limited data loss) - default
     * acks=all: Leader and all replicas ack (no data loss)
     */
    configs.setProperty(ProducerConfig.ACKS_CONFIG, "all");

    /**
     * Number of retries on producing
     */
    configs.setProperty(ProducerConfig.RETRIES_CONFIG, Integer.toString(Integer.MAX_VALUE));

    /**
     * Number of producers trying to produce at the same time
     */
    configs.setProperty(ProducerConfig.MAX_IN_FLIGHT_REQUESTS_PER_CONNECTION, "5");

  }
}
