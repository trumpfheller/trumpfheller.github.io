---
layout: default
---
### Java program using Selenium to do Job search on Linkedin

This program uses 
- the ChromeDriver class to open a Chrome browser and navigate to the LinkedIn Jobs search page. 
- then uses the **By.cssSelector()** method to locate the search input field and enters the job title and location information. 
- After submitting the search, the program uses the **By.xpath()** method to locate the location and job type filters and apply them to the search results.

- then uses the **By.cssSelector()** method to locate the job listings on the page and extracts the job title and company name information using the **WebElement.getText()** method. 
- then prints this information to the console.

```python
import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.interactions.Actions;

import java.util.List;

public class LinkedInJobSearch {

    public static void main(String[] args) {
        // Set up the Chrome driver
        System.setProperty("webdriver.chrome.driver", "/path/to/chromedriver");
        WebDriver driver = new ChromeDriver();

        // Define the job title and location to search for
        String jobTitle = "Software QA Manager";
        String location = "California";

        // Search on LinkedIn
        driver.get("https://www.linkedin.com/jobs/");
        WebElement searchBox = driver.findElement(By.cssSelector("input.jobs-search-box__text-input"));
        searchBox.sendKeys(jobTitle + " " + location);
        searchBox.submit();

        // Filter job results by location and job type
        WebElement allFiltersButton = driver.findElement(By.cssSelector("button.jobs-search-dropdown__trigger-icon"));
        allFiltersButton.click();

        WebElement locationFilter = driver.findElement(By.xpath("//label[contains(text(), 'Location')]/following-sibling::input"));
        locationFilter.sendKeys(location);
        locationFilter.submit();

        WebElement jobTypeFilter = driver.findElement(By.xpath("//label[contains(text(), 'Job Type')]/following-sibling::div"));
        Actions actions = new Actions(driver);
        actions.moveToElement(jobTypeFilter).click().perform();
        List<WebElement> jobTypeOptions = driver.findElements(By.xpath("//li[@role='checkbox']/label"));
        for (WebElement option : jobTypeOptions) {
            if (option.getText().contains("Full-time")) {
                actions.moveToElement(option).click().perform();
                break;
            }
        }

        // Get job listings and print the job title and company name
        List<WebElement> jobListings = driver.findElements(By.cssSelector("li.job-result-card"));
        for (WebElement job : jobListings) {
            WebElement jobTitleElement = job.findElement(By.cssSelector("h3.job-result-card__title"));
            WebElement companyElement = job.findElement(By.cssSelector("a.job-result-card__subtitle-link"));

            String jobTitleText = jobTitleElement.getText();
            String companyText = companyElement.getText();

            System.out.println(jobTitleText + " at " + companyText);
        }

        // Close the browser
        driver.quit();
    }

}
```

### Heads up: 
- This solution is relatively usefull. Since many staffing companies are not from the US, you will find a lot of creativity in the title convention, for instance.To resolve this I might have to add a search function of variations of the combination of the string "Software QA Manager".

