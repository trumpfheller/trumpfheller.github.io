---
layout: default
---

### on Firefox
```java
import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.firefox.FirefoxDriver;

public class GoogleSearch {
public static void main(String[] args) {
// Create a new instance of the Firefox driver
WebDriver driver = new FirefoxDriver();

// Navigate to Google
driver.get("https://www.google.com");
}
}
```
