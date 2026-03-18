---
title: "Lab: Data Transfer"
format:
  html:
    embed-resources: true
---

# Load packages

Remember, it's considered a best practice to load all the packages that your file will use up at the top of the file. If you have not yet installed a package, you will need to do so by running `install.packages("package name")` in the R console. For example, to install the `dplyr` package, you would run `install.packages("dplyr")`. However, you typically **do not** want to type the code to install the package here in your Quarto file because you only need to install the package once on a given computer. Not every time you run your R code.

```{r}
#| label: load-packages
library(dplyr, warn.conflicts = FALSE) # The "warn.conflicts" part is optional
library(readxl)
library(readr)
library(haven)
```

# Overview

The NTRHD is part of a study about the association between chocolate eating habits and academic ability. The study took place at multiple schools, chosen at random, from around the region. Graduate students administered the surveys to students at each school, recorded survey responses electronically, and then emailed them to us. Now, we need your help importing the data into R, doing a little bit of data cleaning, and saving the data again once it’s ready for analysis. 

Additionally, we need you to download, clean, and save some NHANES data on alcohol use.

# Task 1 

Click the links below to download the raw data files to your computer: 

* [chocolate study 1.xls](https://www.dropbox.com/s/9riqfhtf582o2az/Chocolate%20Study%201.xls?dl=1)   
* [chocolate study 2.csv](https://www.dropbox.com/s/ggln051redw1g98/Chocolate%20Study%202.csv?dl=1)
* [chocolate study 3.txt](https://www.dropbox.com/s/90ndmdc463ui88j/Chocolate%20Study%203.txt?dl=1)

# Task 2

Import **Chocolate Study 1.xls** into your R global environment as **choco_1**.

## Question 1

Which of the following code chunks will correctly import the **Chocolate Study 1.xls** data into your R global environment as **choco_1**?

```{r}
#| eval: false

# Incorrect: chocolate_study_1.xls is not a csv file.
choco_1 <- read_csv("Chocolate Study 1.xls")
```

```{r}
#| eval: false

# Incorrect: readxl is the name of an R package, not a function.
choco_1 <- readxl("Chocolate Study 1.xls")
```

```{r}
#| eval: false

# Incorrect: readr is the name of an R package, not a function.
choco_1 <- readr("Chocolate Study 1.xls")
```

```{r}
#| eval: false

# Correct.
choco_1 <- read_excel("Chocolate Study 1.xls")
```

```{r}
# For Dr. Cannell's computer.
choco_1 <- read_excel("/Users/bradcannell/Dropbox/Datasets/Chocolate/Chocolate Study 1.xls")
```

# Task 3 

View the structure of **choco_1** using the `str()` function.

```{r}
str(choco_1)
```

## Question 2

The **choco_1** data frame contains ____ rows and ____ columns.

* The **choco_1** data frame contains 50 rows and 21 columns.

# Task 4

Import **Chocolate Study 2.csv** into your R global environment as **choco_2**.

## Question 3

Which of the following code chunks will correctly import the **Chocolate Study 2.csv** data into your R global environment?

```{r}
#| eval: false

# Incorrect: Although you can open chocolate_study_1.csv in Excel, it doesn't have a .xls or .xlsx file extension, which is what read_excel expects.
choco_2 <- read_excel("Chocolate Study 2.csv")
```

```{r}
#| eval: false

# Incorrect: There is a read.csv() function that will import this data. However, it isn't in the readr package. The double colon syntax used in the code readr::read.csv() tells R to look for the read.csv() function in the readr package, which doesn't exist. The read_csv() function is a base R function. 
choco_2 <- readr::read.csv("Chocolate Study 2.csv")
```

```{r}
#| eval: false

# Correct. However, I prefer read_csv() over read.csv().
choco_2 <- read.csv("Chocolate Study 2.csv")
```

```{r}
#| eval: false

# Correct.
choco_2 <- read_csv("Chocolate Study 2.csv")
```

```{r}
# For Dr. Cannell's computer.
choco_2 <- read_csv("/Users/bradcannell/Dropbox/Datasets/Chocolate/Chocolate Study 2.csv")
```

# Task 5 

View the structure of **choco_2** using the `str()` function.

```{r}
str(choco_2)
```

## Question 4

The **choco_2** data frame contains ____ rows and ____ columns.

* The **choco_2** data frame contains 20 rows and 21 columns.

# Task 6 

Import **Chocolate Study 3.txt** into your R global environment as **choco_3**. Make sure to tell R how to correctly identify missing values in the raw data.

## Question 5

Which of the following code chunks will correctly import the **Chocolate Study 3.txt** data into your R global environment?

```{r}
#| eval: false

# Incorrect: read_table will not correctly handle values that include spaces 
# such as "Flower Grove" in the school column.
choco_3 <- read_table("Chocolate Study 3.txt")
```

```{r}
#| eval: false

# Incorrect: This code does not tell R how to correctly identify missing values in the raw data.
choco_3 <- read_fwf(
  "Chocolate Study 3.txt",
  col_positions = fwf_widths(
    widths    = c(5, 9, 8, 4, 6, 13, 9, 9, 6, 6, 6, 6, 6, 6, 8, 7, 7, 7, 7, 9, 6),
    col_names = c(
      "uin", "last", "first", "age", "grade", "school", "parent", "marry", 
      "math1", "math2", "math3", "read1", "read2", "read3", "overall", "choco1", 
      "choco2", "choco3", "extra1", "extra2", "veggie"
    )
  ),
  skip = 1,
  na.rm = TRUE
)
```

```{r}
#| eval: false

# Incorrect: This code gives column start values instead of column widths
choco_3 <- read_fwf(
  "Chocolate Study 3.txt",
  col_positions = fwf_widths(
    widths    = c(
      1, 6, 15, 23, 27, 33, 46, 55, 64, 70, 76, 82, 88, 94, 100, 108, 115, 122, 
      129, 136, 145
    ),
    col_names = c(
      "uin", "last", "first", "age", "grade", "school", "parent", "marry", 
      "math1", "math2", "math3", "read1", "read2", "read3", "overall", "choco1", 
      "choco2", "choco3", "extra1", "extra2", "veggie"
    )
  ),
  skip = 1,
  na = "."
)
```

```{r}
#| eval: false

# Correct
choco_3 <- read_fwf(
  "Chocolate Study 3.txt",
  col_positions = fwf_widths(
    widths    = c(5, 9, 8, 4, 6, 13, 9, 9, 6, 6, 6, 6, 6, 6, 8, 7, 7, 7, 7, 9, 6),
    col_names = c(
      "uin", "last", "first", "age", "grade", "school", "parent", "marry", 
      "math1", "math2", "math3", "read1", "read2", "read3", "overall", "choco1", 
      "choco2", "choco3", "extra1", "extra2", "veggie"
    )
  ),
  skip = 1,
  na = "."
)
```

```{r}
# For Dr. Cannell's computer.
choco_3 <- read_fwf(
  "/Users/bradcannell/Dropbox/Datasets/Chocolate/Chocolate Study 3.txt",
  col_positions = fwf_widths(
    widths    = c(5, 9, 8, 4, 6, 13, 9, 9, 6, 6, 6, 6, 6, 6, 8, 7, 7, 7, 7, 9, 6),
    col_names = c(
      "uin", "last", "first", "age", "grade", "school", "parent", "marry", 
      "math1", "math2", "math3", "read1", "read2", "read3", "overall", "choco1", 
      "choco2", "choco3", "extra1", "extra2", "veggie"
    )
  ),
  skip = 1,
  na = "."
)
```

# Task 7 

View the structure of **choco_3** using the `str()` function.

```{r}
str(choco_3)
```

## Question 6

The **choco_3** data frame contains ____ rows and ____ columns.

* The **choco_3** data frame contains 10 rows and 21 columns.

# Task 8

Please view the National Health and Nutrition Examination Survey (NHANES) questionnaires, datasets, and related documentation website here: https://wwwn.cdc.gov/nchs/nhanes/Default.aspx. Then, locate and select the **NHANES 2017-2018 data**.

# Task 9

After locating the data from the correct years, import the **Alcohol Use** data into R. 

* **Alcohol Use** was part of the **NHANES questionnaire data**. The link to the data file should be labeled as, "ALQ_J Data [XPT - 434.4 KB]". The **XPT** file extension tells us that this is a SAS Transport file.

* Name the data frame you create **alq_j**.

* Instead of downloading the data from the NHANES website to your computer, try passing a link to the XPT file directly to the `read_xpt()` function. [R4Epi](https://www.r4epi.com/importing-binary-files.html#importing-sas-data-sets) has an example that you can reference. 

```{r}
alq_j <- read_xpt("https://wwwn.cdc.gov/Nchs/Nhanes/2017-2018/ALQ_J.XPT")
```

## Question 7

What R package contains the `read_xpt()` function we need to use to import the NHANES data in Task 9?

* The [haven](https://haven.tidyverse.org/) package contains the `read_xpt()` function we need to use to import the NHANES data in Task 9.

# Task 10. 

Coerce all of the variable names in `alq_j` to lowercase.

## Question 8

Which of the following code chunks will correctly coerce all of the variable names in `alq_j` to lowercase?

```{r}
#| eval: false

# Incorrect: This code passes the entire alq_j data frame, not just the column names from alq_j, to the tolower() function.
names(alq_j) <- alq_j |> tolower()
```

```{r}
#| eval: false

# Incorrect: This code doesn't assign the lowercase variable names back to the alq_j data frame (or anywhere else).
tolower(names(alq_j))
```

```{r}
#| eval: false

# Incorrect: This code overwrites the alq_j data frame with a vector of lowercase variable names from the alq_j data frame.
alq_j <- names(alq_j) |> tolower()
```

```{r}
# Correct.
names(alq_j) <- names(alq_j) |> tolower()
```

## Notes for students

1. We can easily convert any character string to all lowercase letters using the `tolower()` function. The code above tells R to get the column names from alq_j (`names(alq_j)`), convert them all to lowercase (`|> tolower()`), and finally assign the new lowercase versions back to the column names (`names(alq_j) <-`).

# Task 11

Coerce all of the categorical variables in **alq_j** to factor variables. Use the value descriptions from the NHANES Alcohol Use data codebook to make factor levels and labels. Name the factor version of each variable with the same name as the original version, but add a **_f** to the end.

* The codebook for the **Alcohol Use** data is available from the same web page you found the data on. Immediately to the left of was part of "ALQ_J Data [XPT - 434.4 KB]", you should see a linked file called "ALQ_J.Doc". Clicking on that link should open the codebook.

```{r}
# Create a numeric vector you can reuse for all yes/no factor levels
yn_levs <- c(1, 2, 7, 9)

# Create a character vector you can reuse for all yes/no factor labels
yn_labs <- c("Yes", "No", "Refused", "Don't know")

# Create a numeric vector you can reuse for all unit of time factor levels
time_levs <- c(0:10, 77, 99)

# Create a character vector you can reuse for all unit of time factor labels
time_labs <- c(
  "Never in the last year", "Every day", "Nearly every day", 
  "3 to 4 times a week", "2 times a week", "Once a week", 
  "2 to 3 times a month", "Once a month", "7 to 11 times in the last year",
  "3 to 6 times in the last year", "1 to 2 times in the last year",
  "Refused", "Don't know"
)
```

## Notes for students

1. You don't have to create vectors of level values and labels values as I did in the code chunk above. Instead, you could have entered these values directly into the `factor()` functions below -- as I did for **alq130** and **alq170**. I created these vectors of values and labels for a couple of reasons. First, it reduces the amount of typing I have to do in the code chunk below (and makes the code chunk below easier to read). Second, because I'm typing less, the likelihood of me making a typo is reduced. Finally, if I ever need to change the levels or labels, I just change them once in the code chunk above, as opposed to changing every `factor()` function in the code chunk below.

2. Why didn't I create a vector of level values and label values for **alq130** and **alq170**? I didn't create a vector of level values and label values for **alq130** and **alq170** because the values used are unique -- they aren't used by any other variable in the data frame. Therefore, the advantages listed above don't apply (aside from possibly making the code easier to read).

3. Why am I coercing **alq130** and **alq170** to factors? The instructions say to coerce all categorical variables, but **alq130** and **alq170** contain counts of drinks and drinking occasions respectively. If you had this question, it's a good one. And you are partially correct. For **alq130**, values between **1** and **14** (I explain why not 13 in the next bullet) _do_ represent a numeric count value. However, the value **15** is not a count value. When a **15** appears in the data for this variable, it doesn't necessarily mean that a person had 15 drinks. It means that they had 15 OR MORE drinks. So, they could have had 15, 17, or 100. Therefore, this is a _category_ -- not a count -- and in order to analyze this variable in a way that is valid for _all_ responses (i.e., not just the values less than 15), we have to treat this variable as a categorical variable. In the new factor version of **alq130** -- called **alq130_f** -- the values **1** through **14** will still _look_ like numbers, but they will represent categories. The same logic applies to **alq170**. The value **30** means "more than 20 times per month," not "30 times per month."

4. Why did I pass the values `1:14` to the `factor()` function used to create **alq130_f** in the code chunk below instead of `1:13`? If you had this question, you probably paid close attention to the [codebook](https://wwwn.cdc.gov/Nchs/Nhanes/2017-2018/ALQ_J.htm#ALQ130) -- good job! The codebook states that the values **1** to **13** represent a "range of values" (i.e., counts of drinks) and the value **15** represents "15 or more drinks." If you were paying attention, you may have noticed that 14 isn't mentioned anywhere. Why not?? Well, I don't know for sure, but what I do know is that none of the participants have a value of **14** for **alq130**. Because none of the participants have a value of **14** for **alq130** we could simply ignore it, but that makes my skin crawl. Why? There are at least two reasons. First, what if we collected more data and one of the new participants reported having 14 drinks on average? This code would ignore those participants in our analysis. Additionally, even if there is never a participant who reports 14 drinks, we want our analysis results to reflect that 14 drinks was a _possible_ response -- it's just that zero people gave it. If we don't add an explicit level and label for the value **14** in our code, then R will treat it as though it doesn't exist. If you don't believe me, try it out for yourself.

```{r}
alq_j <- alq_j |> 
  mutate(
    alq111_f  = factor(alq111, yn_levs, yn_labs),
    alq121_f  = factor(alq121, time_levs, time_labs),
    alq130_f  = factor(
      alq130, 
      c(1:14, 15, 777, 999), 
      c(1:14, "15 drinks or more", "Refused", "Don't know")
    ),
    alq142_f  = factor(alq142, time_levs, time_labs),
    alq270_f  = factor(alq270, time_levs, time_labs),
    alq280_f  = factor(alq280, time_levs, time_labs),
    alq290_f  = factor(alq290, time_levs, time_labs),
    alq151_f  = factor(alq151, yn_levs, yn_labs),
    alq170_f  = factor(
      alq170,
      c(0:20, 30, 777, 999), 
      c(0:20, "15 drinks or more", "Refused", "Don't know")
    ),
  )
```

# Task 12

View the structure of **alq_j** using the `str()` function.

```{r}
str(alq_j)
```

## Questions 9

The **alq_j** data frame contains ____ rows and ____ columns.

* The **alq_j** data frame contains 5,533 rows and 19 columns.

## Questions 10

When you view the structure of **alq_j** using the `str()` function, what is the vector type shown for **alq111_f**? According to R, what kind of variable is **alq111_f**? 

* When you view the structure of **alq_j** using the `str()` function, the vector type shown is **Factor**.

