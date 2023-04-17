## Python porting of Stochastic TradingView Indicator


>Developed by [@edyatl](https://github.com/edyatl) April 2023 <edyatl@yandex.ru>

### Using [Python wrapper](https://github.com/TA-Lib/ta-lib-python) for [TA-LIB](http://ta-lib.org/) based on Cython instead of SWIG.

### Original Indicator code

```python
//@version=5 
indicator(title="Stochastic", shorttitle="Stoch", format=format.price, precision=2, timeframe="", timeframe_gaps=true) 

periodK = input.int(14, title="%K Length", minval=1) 
smoothK = input.int(1, title="%K Smoothing", minval=1) 
periodD = input.int(3, title="%D Smoothing", minval=1) 

k = ta.sma(ta.stoch(close, high, low, periodK), smoothK) 
d = ta.sma(k, periodD) 

plot(k, title="%K", color=#2962FF) 
plot(d, title="%D", color=#FF6D00) 

h0 = hline(80, "Upper Band", color=#787B86) 

hline(50, "Middle Band", color=color.new(#787B86, 50)) 

h1 = hline(20, "Lower Band", color=#787B86) 

fill(h0, h1, color=color.rgb(33, 150, 243, 90), title="Background")
```
### Original Indicator Overview
This script creates an indicator on a chart that displays the Stochastic Oscillator. The Stochastic Oscillator is a technical analysis tool that compares a security's closing price to its price range over a given time period.

The indicator has three input parameters that can be adjusted: the length of the %K line, the smoothing factor for the %K line, and the smoothing factor for the %D line.

The script uses these parameters to calculate the %K and %D lines, which are plotted on the chart. The %K line is the main line, while the %D line is a signal line that helps to identify potential buy or sell signals.

The indicator also includes three horizontal lines that represent overbought, oversold, and neutral levels. The background between the overbought and oversold levels is filled with a blue color to help visually identify potential trading opportunities.

Traders can use the Stochastic Oscillator to help identify potential overbought or oversold conditions in a security. When the %K line crosses above the %D line in oversold territory, it may be a signal to buy. Conversely, when the %K line crosses below the %D line in overbought territory, it may be a signal to sell.



