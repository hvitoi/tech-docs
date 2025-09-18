package com.hvitoi.demo.controllers;

import java.io.IOException;
import java.net.URI;
import java.net.URISyntaxException;
import java.net.http.HttpClient;
import java.net.http.HttpRequest;
import java.net.http.HttpResponse;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class UrlCheckController {

  private final String SITE_IS_UP = "Site is up!";
  private final String SITE_IS_DOWN = "Site is down!";
  private final String INVALID_URL = "URL is incorrect!";

  private final HttpClient httpClient = HttpClient.newHttpClient();

  @GetMapping("/check")
  public String getUrlStatusMessage(@RequestParam String url) {
    try {
      var uri = new URI(url);
      var request = HttpRequest.newBuilder(uri)
          .GET()
          .build();
      var response = httpClient.send(request, HttpResponse.BodyHandlers.discarding());
      return response.statusCode() == 200 ? SITE_IS_UP : SITE_IS_DOWN;
    } catch (URISyntaxException e) {
      return INVALID_URL;
    } catch (IOException | InterruptedException e) {
      Thread.currentThread().interrupt(); // restore interrupted status
      return SITE_IS_DOWN;
    }
  }

}
