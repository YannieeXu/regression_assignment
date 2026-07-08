args <- commandArgs(trailingOnly=TRUE)
if (length(args) != 3) {
  stop("Usage: Rscript linear_regression_r.R <filename> <x_col> <y_col>")
}

df <- read.csv(args[1])
model <- lm(df[[args[3]]] ~ df[[args[2]]])

slope <- coef(model)[2]
intercept <- coef(model)[1]
r2 <- summary(model)$r.squared

cat("Slope:", round(slope, 4), "\n")
cat("Intercept:", round(intercept, 4), "\n")
cat("R-squared:", round(r2, 4), "\n")

png("linear_regression_r_output.png", width=800, height=600)
plot(df[[args[2]]], df[[args[3]]], main="Linear Regression (AI)", pch=19, col="steelblue")
abline(model, col="red", lwd=2)
dev.off()
cat("Saved: linear_regression_r_output.png\n")
