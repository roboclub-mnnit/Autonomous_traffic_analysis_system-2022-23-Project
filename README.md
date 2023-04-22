# Traffic-Analysis-ML-project
<hr>
<img src="https://user-images.githubusercontent.com/79747698/229343724-9ffa2d01-7c86-4305-b14d-dd788f58a9de.jpeg" alt="Robotics club MNNIT" />
<h3>About</h3>
<p>A ML based project to study various parameters of a particular traffic data given and then to catagorise and plot it.</p>
<hr>
<h3>This project is mentored by:</h3>
<table>
  <tr>
    <th>Name</th>
    <th>Branch</th>
    <th>Registration number</th>
  </tr>
  <tr>
    <td>Kandukuri Yaswanth</td>
    <td>Civil Engineering</td>
    <td>20201057</td>
  </tr>
  <tr>
    <td>Anurag gupta</td>
    <td>Electronics and Communication Engineering</td>
    <td>20195168</td>
  </tr>
 </table>
 <hr>
<h3>This project is completed by</h3>
<table>
  <tr>
    <th>Name</th>
    <th>Branch</th>
    <th>Registration number</th>
  </tr>
  <tr>
    <td>Priyansh Lohiya</td>
    <td>ECE</td>
    <td>20215109</td>
  </tr>
  <tr>
    <td>Aayush Verma</td>
    <td>ECE</td>
    <td>20215056</td>
  </tr>
  <tr>
    <td>Priyanshu Maurya</td>
    <td>EE</td>
    <td>20212021</td>
  </tr>
  <tr>
    <td>Rishi Mishra</td>
    <td>ECE</td>
    <td>20215096</td>
  </tr>
 </table>
<hr>
<h3> Tech Stack </h3>
<ul>
  <li>Python</li>
  <li>OpenCV</li>
  <li>YOLOv8</li>
  <li>Harr cascade</li>
  <li>Jupyter notebook</li>
  <li>Python libraries such as Pandas, Matplotlib, Numpy, Supervision etc</li>
  <li>Tkinter (for making GUI)</li>
  <li>Byte tracker Algorithm library.</li>
 </ul>
<hr>
<h3>The steps involved</h3>
<ol>

<li><h4>Learning Basic Requirements:</li>

Learning Python was the first task since all the work is done using python libraries hence a good understanding of Python is required. We also have to set up the jupyter notebook. 
After Python, we need to learn the basic libraries that are used in our project, and that include Numpy, OpenCV, matplotlib, and Pandas.

<li><h4>Selecting the Model:</li>

Since there are multiple methods and models to detect the objects so selecting the most appropriate model is an essential task for our project. We have tried different methods and models but the most appropriate is Yolov8. It is the most accurate model available to us. Haar Cascade is also helpful but a good dataset for the Haar Cascade is very difficult to find. Some datasets are paid for by Haar Cascade.  

<li><h4>Detection of Required Objects:</li>

For our project, we need to detect the vehicles into 4 categories:
Cars, Buses, Trucks, Bikes. We also have to detect the pedestrian for our task.
We are using Ultralytics' YOLOv8 object detection model for detecting vehicles and a custom implementation of the BYTE Tracker algorithm for tracking the detected vehicles. The video is read frame by frame using the supervision library, and the detection and tracking algorithms process each frame.

![Picture1](https://user-images.githubusercontent.com/97392355/233791441-53edfdc4-e22a-46d3-8219-0d02dd698269.jpg)

Detected vehicles are enclosed in a bounding box.

![Picture2](https://user-images.githubusercontent.com/97392355/233791507-18c1207f-5109-4d75-bbdd-66a3ff34a17e.jpg)

Detected vehicles are given IDs and their type is also detected and      
shown over the bounding box.

![Picture3](https://user-images.githubusercontent.com/97392355/233791516-40542696-4f63-44bb-a5f5-001fb24c9a20.jpg)

Detecting and differentiating whether the vehicle detected is a car,   bike, bus, or truck.

<li><h4>Speed detection:</li>

For spot speed analysis we have to detect the speed of the vehicles. For speed detection, we use the Haar Cascade method to detect the vehicles and then we are measuring the time taken by the vehicle between any two points on the road. Since we already know the distance between the two points so speed=distance/time. This algorithm reads a video file of a traffic scene, detects and tracks vehicles using a Haar cascade classifier and a correlation tracker, and estimates the speed of the vehicles based on their movement between consecutive frames.
Selecting the data set for Haar Cascade is the most critical task. So we need to find the most accurate dataset available.

![Picture4](https://user-images.githubusercontent.com/97392355/233791630-89c9704c-d8ec-41af-8b1f-66fef61fc47d.jpg)

<li><h4>Volume Analysis:</li>

Traffic Volume is defined as the number of vehicles passing a section of a lane or roadway during a given time interval. Traffic volume studies are conducted to determine the number, movements, and classifications of roadway vehicles at a given location. 
We count the number of vehicles in a given time interval and then convert them into their respective PCU (Passenger Car Units) which are traffic variables (such as headway, speed, and density) compared to a single standard passenger car and calculate the volume and peak hourly factor and the data can be presented and analyzed by plotting graphs

![Picture5](https://user-images.githubusercontent.com/97392355/233791658-a36bb2a3-483b-4c55-95ef-1fc569ae12eb.jpg)


<li><h4>Spot Speed Analysis:</li> 

This is a statistical analysis of data we collected from speed detection. In speed detection, we collected the vehicle's number and their speed in an Excel file, now the spot speed Algo. will plot related graphs of the given data. For spot speed analysis we used the matplotlib library of Python.
Graph 1: Speed vs Frequency.

![Picture6](https://user-images.githubusercontent.com/97392355/233791676-81f8b67d-7fb2-4632-8079-050d54f7b48a.png)


Graph 2: Speed vs Cumulative Frequency.

![Picture7](https://user-images.githubusercontent.com/97392355/233791691-dbc8f311-5e5c-4ff0-8570-3500f724af14.png)


<li><h4>GUI:</li> 

Now all the above steps will finally be executed in Graphical User Interface.

![Picture8](https://user-images.githubusercontent.com/97392355/233791703-c23fd083-5a55-4b69-8386-43ea162ae4fe.jpg)

Our GUI has the Following features:
An upload button to upload the video we want to analyze.
After uploading the video download button to download the result pdf of the volume study and spot speed analysis.
And lastly, two buttons to see the result videos. One for vehicle detection video and the second for speed detection.
</ol>
