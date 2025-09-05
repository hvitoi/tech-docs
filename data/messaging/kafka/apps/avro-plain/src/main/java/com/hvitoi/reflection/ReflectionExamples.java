package com.hvitoi.reflection;

import org.apache.avro.Schema;
import org.apache.avro.file.DataFileReader;
import org.apache.avro.file.DataFileWriter;
import org.apache.avro.io.DatumReader;
import org.apache.avro.io.DatumWriter;
import org.apache.avro.reflect.ReflectData;
import org.apache.avro.reflect.ReflectDatumReader;
import org.apache.avro.reflect.ReflectDatumWriter;

import java.io.File;
import java.io.IOException;

public class ReflectionExamples {

    public static void main(String[] args) {
        // Here we use reflection to determine the schema from a plain java class
        Schema schema = ReflectData.get().getSchema(ReflectedCustomer.class);
        System.out.println("schema = " + schema.toString(true));

        // Write Reflected Record to an AVRO file (binary format)
        DatumWriter<ReflectedCustomer> writer = new ReflectDatumWriter<ReflectedCustomer>(ReflectedCustomer.class);
        try {
            // Open file writer
            DataFileWriter<ReflectedCustomer> dataFileWriter = new DataFileWriter<ReflectedCustomer>(writer); //.setCodec(CodecFactory.deflateCodec(9));

            // Add data
            dataFileWriter.create(schema, new File("customer-reflected.avro"));
            dataFileWriter.append(new ReflectedCustomer("Bill", "Clark", "The Rocket"));    
            System.out.println("File Written (customer-reflected.avro)");

            // Close file writer
            dataFileWriter.close();
        } catch (IOException e) {
            e.printStackTrace();
        }

        // Read Reflected Record from AVRO file (binary format)
        final File file = new File("customer-reflected.avro");
        final DatumReader<ReflectedCustomer> reader = new ReflectDatumReader<ReflectedCustomer>(ReflectedCustomer.class);
        try {
            // Open file reader
            DataFileReader<ReflectedCustomer> dataFileReader = new DataFileReader<ReflectedCustomer>(file, reader);

            for (ReflectedCustomer reflectedCustomer : dataFileReader) {
                System.out.println("Reading reflected record");
                System.out.println(reflectedCustomer.fullName());
            }

            // Close file reader
            dataFileReader.close();
        } catch (IOException e) {
            e.printStackTrace();
        }

    }
}
