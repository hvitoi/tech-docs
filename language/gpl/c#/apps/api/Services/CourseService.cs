using Azure.Storage.Blobs;
using Microsoft.AspNetCore.Hosting;
using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Text;
using System.Text.Json;
using System.Threading.Tasks;
using MyApi.Models;

namespace MyApi.Services
{
    public class CourseService
    {
        public IWebHostEnvironment _env;
        private string connectionString = "DefaultEndpointsProtocol=https;AccountName=hvitoi;AccountKey=uIMNeNSWvPCdd+9OqW2ISdL/GjVPtseBEh5L94zpx/NlbTk8Tnasxxe/SWRZkfa9AgFtZTgw8ATEQNI2+XvMPA==;EndpointSuffix=core.windows.net";
        public IEnumerable<Course> GetCourses()
        {
            BlobServiceClient blobServiceClient = new BlobServiceClient(connectionString);
            BlobContainerClient containerClient = blobServiceClient.GetBlobContainerClient("data");
            BlobClient blobClient = containerClient.GetBlobClient("Courses.json");

            var response = blobClient.Download();
            var l_reader = new StreamReader(response.Value.Content);
            return JsonSerializer.Deserialize<Course[]>(l_reader.ReadToEnd());
        }

        public Course GetCourse(string p_course)
        {

            IEnumerable<Course> courses = this.GetCourses();
            Course course=courses.FirstOrDefault(m => m.CourseID == p_course);
            return course;
        }
        

        public void AddCourse(Course course)
        {
            Course[] courses;
            BlobServiceClient blobServiceClient = new BlobServiceClient(connectionString);
            BlobContainerClient containerClient = blobServiceClient.GetBlobContainerClient("data");
            BlobClient blobClient = containerClient.GetBlobClient("data.json");

            var response = blobClient.Download();
            var l_reader = new StreamReader(response.Value.Content);
            courses = JsonSerializer.Deserialize<Course[]>(l_reader.ReadToEnd());

            List<Course> courselist = courses.ToList<Course>();

            courselist.Add(course);

            // write the new list of courses
            var output = JsonSerializer.Serialize(courselist, new JsonSerializerOptions{WriteIndented=true});
            var content = Encoding.UTF8.GetBytes(output);
            using (var ms = new MemoryStream(content)) blobClient.Upload(ms,overwrite:true);
        }
    }
}
