-- ค่า AQI สูงสุดในสัปดาห์นี้
SELECT MAX(aqi) FROM aqi_data WHERE timestamp >= NOW() - INTERVAL '7 days';

-- ค่า AQI ต่ำสุดในช่วง 3 เดือน
SELECT MIN(aqi) FROM aqi_data WHERE timestamp >= NOW() - INTERVAL '3 months';

-- ค่าเฉลี่ย AQI สัปดาห์นี้
SELECT AVG(aqi) FROM aqi_data WHERE timestamp >= NOW() - INTERVAL '7 days';

-- ค่า AQI รายวันของสัปดาห์นี้
SELECT DATE(timestamp), AVG(aqi) FROM aqi_data 
WHERE timestamp >= NOW() - INTERVAL '7 days'
GROUP BY DATE(timestamp);

-- เขตที่มี AQI สูงสุดในเดือนที่ผ่านมา
SELECT city, MAX(aqi) FROM aqi_data 
WHERE timestamp >= NOW() - INTERVAL '1 month'
GROUP BY city ORDER BY MAX(aqi) DESC LIMIT 1;
