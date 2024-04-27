package com.hvitoi.evolution;

import com.example.CustomerV1;
import com.example.CustomerV2;
import org.apache.avro.file.DataFileReader;
import org.apache.avro.file.DataFileWriter;
import org.apache.avro.io.DatumReader;
import org.apache.avro.io.DatumWriter;
import org.apache.avro.specific.SpecificDatumReader;
import org.apache.avro.specific.SpecificDatumWriter;

import java.io.File;
import java.io.IOException;

public class SchemaEvolutionExamples {
    public static void main(String[] args) throws IOException {

        /**
         * Let's test a backward compatible read
         */

        // Version 1 Customer
        CustomerV1 customerV1 = CustomerV1.newBuilder()
                .setAge(34)
                .setAutomatedEmail(false)
                .setFirstName("John")
                .setLastName("Doe")
                .setHeight(178f)
                .setWeight(75f)
                .build();
        System.out.println("Customer V1: " + customerV1.toString());

        // Write it out to a avro file
        final DatumWriter<CustomerV1> writer = new SpecificDatumWriter<CustomerV1>(CustomerV1.class);
        final DataFileWriter<CustomerV1> dataFileWriter = new DataFileWriter<CustomerV1>(writer);
        dataFileWriter.create(customerV1.getSchema(), new File("customer-v1.avro"));
        dataFileWriter.append(customerV1);
        dataFileWriter.close();
        System.out.println("File Written (customer-v1.avro)");

        // Read the v1 avro file using the v2 schema
        System.out.println("Reading customerV1.avro with v2 schema");
        final File fileV1 = new File("customer-v1.avro");
        final DatumReader<CustomerV2> readerV2 = new SpecificDatumReader<CustomerV2>(CustomerV2.class);
        final DataFileReader<CustomerV2> dataFileReaderV2 = new DataFileReader<CustomerV2>(fileV1, readerV2);
        while (dataFileReaderV2.hasNext()) {
            CustomerV2 customerV2read = dataFileReaderV2.next();
            System.out.println("Customer V2: " + customerV2read.toString());
        }
        dataFileReaderV2.close();

        System.out.println("Backward schema evolution successful\n\n\n");


        /**
         * Let's test a forward compatible read
         */

        // Version 2 Customer
        CustomerV2 customerv2 = CustomerV2.newBuilder()
                .setAge(25)
                .setFirstName("Mark")
                .setLastName("Simpson")
                .setEmail("mark.simpson@gmail.com")
                .setHeight(160f)
                .setWeight(65f)
                .setPhoneNumber("123-456-7890")
                .build();
        System.out.println("Customer V2: " + customerv2.toString());

        // Write it out to a avro file
        final DatumWriter<CustomerV2> datumWriterV2 = new SpecificDatumWriter<CustomerV2>(CustomerV2.class);
        final DataFileWriter<CustomerV2> dataFileWriterV2 = new DataFileWriter<CustomerV2>(datumWriterV2);
        dataFileWriterV2.create(customerv2.getSchema(), new File("customer-v2.avro"));
        dataFileWriterV2.append(customerv2);
        dataFileWriterV2.close();
        System.out.println("File Written (customer-v2.avro)");

        // Read the v2 avro file using the v1 schema
        System.out.println("Reading our customerV2.avro with v1 schema");
        final File fileV2 = new File("customer-v2.avro");
        final DatumReader<CustomerV1> readerV1 = new SpecificDatumReader<CustomerV1>(CustomerV1.class);
        final DataFileReader<CustomerV1> dataFileReaderV1 = new DataFileReader<CustomerV1>(fileV2, readerV1);
        while (dataFileReaderV1.hasNext()) {
            CustomerV1 customerV1Read = dataFileReaderV1.next();
            System.out.println("Customer V1: " + customerV1Read.toString());
        }
        dataFileReaderV1.close();

        System.out.println("Forward schema evolution successful");

    }
}
