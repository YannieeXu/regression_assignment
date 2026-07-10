args <- commandArgs(trailingOnly=TRUE)
if (length(args) != 3) {
  stop("Usage: Rscript linear_regression_r.R <filename> <x_column> <y_column>")
}

filename <- args[1]
x_col <- args[2]
y_col <- args[3]

df <- read.csv(filename)
model <- lm(df[[y_col]] ~ df[[x_col]])

slope <- coef(model)[2]
intercept <- coef(model)[1]
r2 <- summary(model)$r.squared

cat("Slope:", round(slope, 4), "
")
cat("Intercept:", round(intercept, 4), "
")
cat("R-squared:", round(r2, 4), "
")

png("linear_regression_r_output.png", width=800, height=600)
plot(df[[x_col]], df[[y_col]], main="Salary vs Experience",
     xlab=x_col, ylab=y_col, pch=19, col="blue")
abline(model, col="red", lwd=2)
dev.off()
cat("Saved: linear_regression_r_output.png
")
