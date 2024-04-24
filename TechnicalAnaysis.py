from tradingview_ta import TA_Handler, Interval

def get_technical_analysis(symbol, exchange, interval):
    try:
        handler = TA_Handler(
            symbol=symbol,
            exchange=exchange,
            screener="america",
            interval=interval
        )
        analysis = handler.get_analysis()

        if not analysis:
            print(f"No analysis available for {symbol} on {exchange} exchange with interval {interval}.")
            return

        summary = analysis.summary
        oscillators = analysis.oscillators
        moving_averages = analysis.moving_averages
        indicators = analysis.indicators

        print(f"\nSymbol: {symbol}")
        print(f"Exchange: {exchange}")
        print(f"Interval: {interval}")
        print("\nTechnical Analysis Summary:")
        print(summary)
        print("\nOscillators:")
        print(oscillators)
        print("\nMoving Averages:")
        print(moving_averages)
        print("\nIndicators:")
        print(indicators)
    except Exception as e:
        print(f"Error fetching data for {symbol} on {exchange} exchange with interval {interval}: {e}")

def main():
    try:
        symbols = input("Enter the stock symbols separated by comma (e.g., AAPL,MSFT): ").split(',')
        exchanges = input("Enter the exchanges separated by comma (e.g., nasdaq,nyse): ").split(',')
        intervals = input("Enter the intervals separated by comma (e.g., 1d,1h): ").split(',')

        for symbol in symbols:
            for exchange in exchanges:
                for interval in intervals:
                    get_technical_analysis(symbol.strip().upper(), exchange.strip().lower(), interval.strip().lower())
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
