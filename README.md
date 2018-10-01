# Working-with-Digi-Device-Cloud
Digi Device Manager provides a standard HTTP Web API service which allows many ways to access data. This is an easy to use reference Python implementation to access data from Digi Device manager API
Digi Device Cloud / Remote Manager is a cloud-based device management platform that allows to connect any device to any application, anywhere. Device Cloud allows users to remotely manage thousands of deployed devices, supporting features like remote firmware upgrades and event alarms.
Devices are associated with the server through the Internet or other wide area network connection, which allows for communication between the device, server, and the customer applications. An important part of this communication is the transfer of data from a device to the server.
The Web API is very easy to use. Device Manager's data streams service is a RESTful API for storing and accessing time series data in Device Manager. The DataPoint API can return a list of timestamped values for a specific data stream and can include metadata such as the description and location, if included when the data was created. By provisioning this API, you can query time series data in Device Manager.

Selecting the right endpoint
The Web API has several endpoints. An endpoint is a server route used to retrieve different data from the API. For example, the /data point endpoint on the API retrieve data points from the specified data stream. To access them, you would add the endpoint to the base url of the API.
The base url for our web API is "https://remotemanager.digi.com/ws/, so we'll add this to the beginning of all of our endpoints.

The data stream for your XBee gateway can be found by adding the device ID for your XBee gateway, for example: "https://remotemanager.digi.com/ws/DataPoint/00000000-00000000-00409DFF-FF63DD73/xbee.serialIn/[00:13:A2:00:41:4F:7F:0F]!.json

Working with JSON data
The content of the response is in JavaScript Object Notation(JSON). JSON is a way to encode data structures like lists and dictionaries to strings that ensures that they are easily readable by machines. JSON is the primary format in which data is passed back and forth to APIs, and most API servers will send their responses in JSON format.Python has great JSON support, with the json package. The json package is part of the standard library, so we don't have to install anything to use it.

Query Parameters
The datapoint endpoint can have several parameters like startTime, endTime, size, order and so on.
We can make a dictionary with these parameters, and then pass them into the requests.get function.
We can also do the same thing directly by adding the query parameters to the url, like this: "https://remotemanager.digi.com/ws/DataPoint/00000000-00000000-00409DFF-FF63DD73/xbee.serialIn/[00:13:A2:00:41:4F:7F:0F]!.json?order=desc&size=100"

It's almost always preferable to setup the parameters as a dictionary because requests take care of some things that come up, like properly formatting the query parameters.
