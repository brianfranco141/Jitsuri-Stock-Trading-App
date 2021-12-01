# Jitsuri Stock-Trading-App
what is Jitsuri you might say? 
An open-source full stack algorithmic trading application that is fast, robust, and scalable. Includes various functions for custom alerts on positions made on Jitsuri via sms text and email. Why reinvent the wheel when powerful api services such as Trading View exist! Jisturi front-end offers high functional charting of stocks and pricing thanks to Trading-View!


Why Alpaca as a brokerage?
Whats unique and special about Alpaca and why I have gone ahead and used it is that there exists a back-testing environment that can is simple to use compared to conventional brokerages due to having the option of swithcing between actual trading and paper-trading capablities offered. Paper trading is using sythetic funds to purchase stocks with real-time markets which can be very benefical in not risking any actual funds,

Note: It is not required to use alpaca trading brokerage for this application, various borkerage platform offer other api services you can implement within Jitsuri easily. Just will need to outsource for stock and price data, since we use Alpaca that kindly offers minute data for free unlike many other services. 

Provided a simple opening range breakout stategy with an example of of how buy and sell orders are executed with alpaca trading api, for more details please read alpaca docs found here https://alpaca.markets/docs/ on how to intereact with Alpaca effectivly. 

Requirments:
linux environment preferred
Tools needed to install in order to run: 
1. Sqlite3 - found here: https://docs.python.org/3/library/sqlite3.html
2. Alpaca trading account - found here and free to sign up: https://alpaca.markets/
3. tulipy - found here - https://pypi.org/project/tulipy/ (pip install tulipy)
4. numpy 1.21.4 - found here - https://pypi.org/project/numpy/ (pip install numpy)
5. Uvicorn -found here - https://www.uvicorn.org/ (pip install uvicorn)


Setup is fairly stright forward

Instructions:
1. Go to the config file and there will be detailed instructions on how the setup with the brokerage is done
1. Run the python file create_db.py to create the database for Jistsuri.
2. Need to populate the database with both stocks and prices. 
   Note: Need to populate stocks before being able to add prices. Has to run in in a specific order
   First run populate_stocks.py
   Second run populate_prices.py
3. run "server startup:  uvicorn main:app --reload" to setup the frontend of the locally hosted webserver 

Contributing to Jitsuri!

Feel free to just tackle any issues that we have/ need to be completed

After create a pull-requests and wait for approval to merge to our main branch.

If you have any creative ideas or impromvents as well, feel free to create a brand new issue or contact me at Jisturi.trading.log@gmail.com





