using Microsoft.AspNetCore.Mvc;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using MyApi.Models;
using MyApi.Services;

namespace MyApi.Controllers
{
    [ApiController]
    [Route("/api/Course")]
    public class CourseController : ControllerBase
    {
        private readonly CourseService courseService;
        public CourseController(CourseService _svc)
        {
            // Dependencies must be defined in Startup.cs (ConfigureServices method)
            courseService = _svc; // Inject CourseService dependency
        }

        // Index page
        // public IActionResult Index()
        // {
        //     return View();
        // }

        [HttpGet] // /api/Course
        public IActionResult GetCourses()
        {
            return Ok(courseService.GetCourses());
        }


        [HttpGet("{id}")] // /api/Course/{id}
        public IActionResult GetCourse(string id)
        {
            return Ok(courseService.GetCourse(id));
        }

        [HttpPost] // /api/Course
        public IActionResult AddCourse(Course course)
        {
            courseService.AddCourse(course);
            return Ok("Added");
        }
    }
}