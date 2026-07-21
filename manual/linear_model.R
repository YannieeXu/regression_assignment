args <- commandArgs(trailingOnly = TRUE)
if (length(args) != 3) {
  stop("Usage: Rscript linear_model.R <filename> <x_column> <y_column>")
}
filename <- args[1]
x_col <- args[2]
y_col <- args[3]
data <- read.csv(filename)
x <- data[[x_col]]
y <- data[[y_col]]
model <- lm(y ~ x)
slope <- coef(model)[2]
intercept <- coef(model)[1]
r <- cor(x, y)
pred <- predict(model)
mse <- mean((y - pred)^2)
cat("Slope:", round(slope, 4), "\n")
cat("Intercept:", round(intercept, 4), "\n")
cat("Correlation coefficient (r):", round(r, 4), "\n")
cat("MSE:", round(mse, 4), "\n")
library(ggplot2)
p <- ggplot(data, aes_string(x = x_col, y = y_col)) +
  geom_point(color = "red") +
  geom_smooth(method = "lm", se = FALSE, color = "blue") +
  annotate("text", x = min(x) + 0.1 * (max(x) - min(x)), y = max(y) * 0.95,
           label = paste("y =", round(slope, 2), "x +", round(intercept, 2), "\nr =", round(r, 2), "\nMSE =", round(mse, 2)),
           hjust = 0, size = 4) +
  labs(title = paste(y_col, "vs", x_col), x = x_col, y = y_col) +
  theme_minimal()
ggsave("regression_plot_r.png", p, width = 7, height = 5)
print(p)
