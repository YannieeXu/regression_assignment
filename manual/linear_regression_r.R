args <- commandArgs(trailingOnly = TRUE)
if (length(args) != 3) {
  stop("Usage: Rscript linear_regression_r.R <filename> <x_column> <y_column>")
}

filename <- args[1]
x_column <- args[2]
y_column <- args[3]

data <- read.csv(filename)
formula <- as.formula(paste(y_column, "~", x_column))
model <- lm(formula, data = data)

cat("Slope:", round(coef(model)[2], 4), "\n")
cat("Intercept:", round(coef(model)[1], 4), "\n")  
cat("R-squared:", round(summary(model)$r.squared, 4), "\n")

library(ggplot2)
plot <- ggplot(data, aes_string(x = x_column, y = y_column)) +
  geom_point(color = "red") +
  geom_smooth(method = "lm", color = "blue") +
  ggtitle(paste(y_column, "vs", x_column)) +
  xlab(x_column) +
  ylab(y_column)

ggsave("linear_regression_r_output.png", plot)
print(plot)
