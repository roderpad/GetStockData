import yfinance as yf

slack = yf.Ticker("WORK") # WORK is the ticker for Slack

history = slack.history(period="max") # Get the slack stock price history with max period

print('The output type is:')
print(type(history)) # Prints the type that history outputs
print('')
print('The history output is the following:')
print(history) # Prints history
print('The csv output of history is the following:')
print(history.to_csv(index=False, line_terminator='\n')) # Prints history as .csv file. Only need index and line_terminatory options if using Windows...
# To create [filename].csv for this output, run 'python DataSources/yahoo.py > [filename].csv