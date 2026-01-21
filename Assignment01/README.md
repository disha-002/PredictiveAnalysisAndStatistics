# Assignment 1: PDF Estimation using NO₂ Data

## Objective

In this assignment we use, NO₂ concentration data to see how we can estimate a probability density function after we change the data in a nonlinear way. The main goal of this is to understand how the data distribution changes when we apply a nonlinear transformation.

---

## Dataset

I used the India Air Quality dataset for this assignment. The NO₂ concentration column was extracted , which was taken as \(x\). Before starting the analysis, the rows with missing values (NA) were removed.

---

## Methodology

### Data Preprocessing

The dataset was loaded and then it was checked for missing NO₂ values. We only picked the NO₂ concentration values. If a row had a missing NO₂ value, it was removed. This way the data we used for the PDF estimation was clean and suitable for analysis.

### Transformation

After we got the data ready, the NO2 values were changed using the formula that was given in the question:

$\hat{p}(z) = c e^{-\lambda (z - \mu)^2}$

The university roll number was used to figure out the values of \(a_r\) and \(b_r\). This change makes a difference to the data that is not linear. The new values are still pretty close to the original NO₂ values. The transformation does not change the NO₂ values drastically.

### Probability Density Function

The transformed values \(z\) were modeled using the following probability density function:

\[

\hat{p}(z) = c \, e^{-\lambda (z - \mu)^2}

\]

We estimated the parameters using basic statistical ideas. The mean of \(z\) was taken as \( \mu \). We then calculate the variance of \(z\). We used this variance to calculate \( \lambda \). The value of \(c\) was chosen so that the total area under the curve adds up to one, making it valid.

---

## Results

### Parameter Values

μ = 25.80962289781127 

λ = 0.0014604365254890003

c = 0.021560876239314915

---

## Result Graph

A histogram and an estimated probability density function were plotted to see the distribution of the data and compare it with the function.

Looking at the graph, we can see that the curve is highest near the average value of \(z\). Then it starts to go down as the values get away from the mean. This means the probability density function does a good job of showing what the transformed data looks like.

---

## Conclusion

In this assignment, a non-linear transformation was applied to NO₂ concentration data, and a probability density function was estimated for the transformed values. The parameters were calculated using simple statistical methods, and the final result was verified using a graphical comparison.