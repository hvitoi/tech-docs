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
     * acks=0: won't wait for ack (possible data loss) - dangerous!
     * fire and forget (the retry config is ignored)
     * 
     * acks=1: wait for leader ack (limited data loss) - default
     * 
     * acks=all: wait for leader ack + n backup replicas (as defined in
     * min.insync.replicas). It will only be considered as produced when all the
     * necessary replicas are in sync
     * 
     */
    configs.setProperty(ProducerConfig.ACKS_CONFIG, "all");

    /**
     * Number of retries on producing
     */
    configs.setProperty(ProducerConfig.RETRIES_CONFIG, Integer.toString(Integer.MAX_VALUE));

    /**
     * Number of producers trying to produce at the same time
     * 
     * How many connections can be active
     * waiting for acknowledgement. More than this, the connection is refused.
     * Default to 5 in parallel. If set to 1 the producer is guaranteed to send
     * messages in order!
     */
    configs.setProperty(ProducerConfig.MAX_IN_FLIGHT_REQUESTS_PER_CONNECTION, "5");

  }
}
