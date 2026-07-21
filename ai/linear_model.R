args <- commandArgs(trailingOnly = TRUE)
if (length(args) != 3) {
  stop("Usage: Rscript linear_model.R <filename> <x_column> <y_column>")
}
data <- read.csv(args[1])
x <- data[[args[2]]]
y <- data[[args[3]]]
model <- lm(y ~ x)
s <- coef(model)
pred <- predict(model)
mse <- mean((y - pred)^2)
r <- cor(x, y)
cat("Slope:", round(s[2], 4), "\n")
cat("Intercept:", round(s[1], 4), "\n")
cat("Correlation coefficient (r):", round(r, 4), "\n")
cat("MSE:", round(mse, 4), "\n")
library(ggplot2)
p <- ggplot(data, aes_string(x = args[2], y = args[3])) +
  geom_point(color = "red", size = 2) +
  geom_smooth(method = "lm", se = FALSE, color = "blue", linewidth = 1) +
  annotate("text", x = min(x), y = max(y),
           label = sprintf("y = %.2fx + %.2f\nr = %.2f\nMSE = %.0f", s[2], s[1], r, mse),
           hjust = 0, vjust = 1, size = 4) +
  labs(title = "Linear Regression with Diagnostics", x = args[2], y = args[3]) +
  theme_bw()
ggsave("regression_plot_r.png", p, width = 8, height = 5)
print(p)
