# Streaming Telemetry For CISCO IOS-XR devices (ASR9k - NCS)

Model-Driven Telemetry is a new approach for network monitoring in which data is streamed from network devices continuously using a push model and provides near real-time access to operational statistics. Applications can subscribe to specific data items they need, by using standard-based YANG data models over NETCONF-YANG.

[cisco-telemetry-tutorial](https://ultraconfig.com.au/blog/cisco-telemetry-tutorial-with-telegraf-influxdb-and-grafana/) 

### Telemetry Solution

We have configured telegraf to collect cpu and memory utilization besides that we get some interfaces statistics also QOS statistics from cisco routers ASR9k with SW IOS-XR, then logging these metrices in TSDB (influxdb) and our analysis and dashboards was built on Grafana.
#### Files in this PJ
> Telegraf_tcp.conf : telegraf configuration file .

> if_desc.py : python script to ssh for routers and switches then map interface name with interface description and interface index for some purposes in data logging and queries it uses nodes.csv file that contain router name and its ip and genertate CSV and Json file .

![HLD](https://github.com/MichaelTharwat/Cisco_telemetry_PJ/blob/main/HLD.png)

### Dashboard Samples

![home](https://github.com/MichaelTharwat/Cisco_telemetry_PJ/blob/main/Grafana_Sample1.jpg)
![cpu](https://github.com/MichaelTharwat/Cisco_telemetry_PJ/blob/main/Grafana_Sample2.jpg) 
![interface](https://github.com/MichaelTharwat/Cisco_telemetry_PJ/blob/main/Grafana_Sample3.jpg)










[def]: https://drive.google.com/file/d/1UnoTmC90xl_THNoeIC9gtr2G3g4trBR1/view?usp=sharing