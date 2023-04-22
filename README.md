<h1>Autonomus traffic analysis system</h1>
<hr>
<img src="https://user-images.githubusercontent.com/79747698/229343724-9ffa2d01-7c86-4305-b14d-dd788f58a9de.jpeg" alt="Robotics club MNNIT" />
<h3>About</h3>
<p>This is a computer vision, ML and DL based project, which is aimed to analyse various parameters of Indian traffic and facilitates the civil engineers to derive required parameters from traffic analysis which helps in calculating quantitative requirements for road upgradation and traffic flow analysis by avaoiding labourus work and also for various other different applications</p>
<br>
<p>In this project the traffic analysis is divided into two parts</p>
<ol>
  <li>Traffic flow analysis</li>
  <li>Spot Speed analysis of traffic</li>
</ol>
<table>
  <tr>
  <td>Traffic flow analysis</td> 
  <td>Here the volume of the traffic flow is analysed and peak hour factor is measured</td>
  </tr>
  <tr>
  <td>Spot Speed analysis of traffic</td> 
  <td>Here the rate of the traffic flow is analysed and percent cumulative frequency distribution graph is plotted from collected data</td>
  </tr>
</table>
<a href="https://docs.google.com/document/d/1n_gXdtBe2LF243WBo5BN1fuVyLqrwQCHrWZPhU2sN3I/edit?usp=sharing">Project report</a>
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
    <td>Electronics and Communication Engineering</td>
    <td>20215109</td>
  </tr>
  <tr>
    <td>Aayush Verma</td>
    <td>Electronics and Communication Engineering</td>
    <td>20215056</td>
  </tr>
  <tr>
    <td>Priyanshu Maurya</td>
    <td>Electrical Engineering</td>
    <td>20212021</td>
  </tr>
  <tr>
    <td>Rishi Mishra</td>
    <td>Electronics and Communication Engineering</td>
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
<br>
<hr>
<h3>Follow the steps:-</h3>

<h4><i>Python version >=3.9 is recommmended</i></h4>
<ol>
<li><p>Clone this repository "https://github.com/ifzhang/ByteTrack" into Vehicle Detection folder and install all the libraries mentioned in requirements.txt inside BYTE tracker repo</p></li>
<li><p>Install ultralytics,cython_bbox,IPython,supervision,onemetric,tqdm,customtkinter library using pip</p></li>
<li><p>Now move to gui folder and run gui.py</p></li>
</ol>

<h3>The steps involved</h3>
<ol>
<li>
<div>
  <h4>Selecting the Model:</h4>
  <p>There are multiple methods and models to detect the objects so selecting the most appropriate model is an essential task for project. YOLO V8 has been used in the project which works on neural networks and the recent 8th version has best efficiency when compared to other models available in the community. Haar Cascade is another ML based model which is helpful in detecting objects but the efficiency is less when compared to YOLO.</p>
</div>
</li>
<li>
<div>
  <h4>Detection of Required Objects:</h4>
  <p>The Indian vehicles are classified into 4 categories:</p>
  <ol>
    <li>Two wheeler</li>
    <li>Three wheeler</li>
    <li>Four wheeler</li>
    <li>Bus
      <ul>
      <li>Mini</li>
      <li>Full</li>
      </ul>
    </li>
  </ol>
<p>YOLO object detection model for detecting vehicles and a custom implementation of the BYTE Tracker algorithm for tracking the detected vehicles. The video is read frame by frame using the supervision library, and the detection and tracking algorithms process each frame</p>
</div>
</li>
<img src="https://user-images.githubusercontent.com/97392355/233791441-53edfdc4-e22a-46d3-8219-0d02dd698269.jpg" alt="picture 1">
<p>Detected vehicles are enclosed in a bounding box</p>
<img src="https://user-images.githubusercontent.com/97392355/233791507-18c1207f-5109-4d75-bbdd-66a3ff34a17e.jpg" alt="picture 2">
<p>Detected vehicles are given IDs and their type is also detected and shown over the bounding box. Detecting and differentiating whether the vehicle detected is a car, bike, bus, or truck</p>
<li>
<div>
  <h4>Speed detection</h4>
  <p>The speed of the vehicles has to be detected in spot speed analysis. In speed detection, the Haar Cascade method is used to detect the vehicles and then we are measuring the time taken by the vehicle between any two points on the road. Since we already know the distance between the two points so speed=distance/time. This algorithm reads a video file of a traffic scene, detects and tracks vehicles using a Haar cascade classifier and a correlation tracker, and estimates the speed of the vehicles based on their movement between consecutive frames.</p>
</div>
</li>
<img src="https://user-images.githubusercontent.com/97392355/233791630-89c9704c-d8ec-41af-8b1f-66fef61fc47d.jpg" alt="picture 4">

<li>
<div>
<h4> Traffic flow Analysis </h4>
<p>Traffic Volume is defined as the number of vehicles passing a section of a lane or roadway during a given time interval. Traffic volume studies are conducted to determine the number, movements, and classifications of roadway vehicles at a given location. We count the number of vehicles in a given time interval and then convert them into their respective PCU (Passenger Car Units) which are traffic variables (such as headway, speed, and density) compared to a single standard passenger car and calculate the volume and peak hourly factor and the data can be presented and analyzed by plotting graphs </p>
</div>
</li>
<img src="https://user-images.githubusercontent.com/97392355/233791658-a36bb2a3-483b-4c55-95ef-1fc569ae12eb.jpg" alt="picture 5">

<li>
<div><h4>Spot Speed Analysis</h4>
<p>This is a statistical analysis of data we collected from speed detection. In speed detection, we collected the vehicle's number and their speed in an Excel file, now the spot speed Algo. will plot related graphs of the given data. For spot speed analysis we used the matplotlib library of Python.</p></li> 


<h4>Graph 1: Speed vs Frequency</h4>
<img src="https://user-images.githubusercontent.com/97392355/233791676-81f8b67d-7fb2-4632-8079-050d54f7b48a.png" alt="picture 6">

<h4>Graph 2: Speed vs Cumulative Frequency</h4>
<img src="https://user-images.githubusercontent.com/97392355/233791691-dbc8f311-5e5c-4ff0-8570-3500f724af14.png" alt="picture 7">

<li><div>
<h4>GUI</h4>
<p>Now all the above steps will finally be executed in Graphical User Interface.</p>
<ul>
<p>Our GUI has the Following features:</p>
<li>An upload button to upload the video we want to analyze.</li>
<li>After uploading the video download button to download the result pdf of the volume study and spot speed analysis.</li>
<li>Last two buttons to see the result videos. One for vehicle detection video and the second for speed detection.</li>
</ul>
</div>
</li> 
<img src="https://user-images.githubusercontent.com/97392355/233791703-c23fd083-5a55-4b69-8386-43ea162ae4fe.jpg" alt="GUI">
</ol>
<br>
<hr>
<h3>Real-life Applications</h3>
<p>The project finds a large spectrum of real-life areas of application</p>

<ul>
<li>To study the type of traffic passing a particular road,  its volume studies and spot speed analysis which facilitates in determining the majority of traffic passing the road, to determine the busiest hours of the road and its traffic density.</li>
<li>The speed detection of vehicles can help in maintaining traffic rules and reduce accidents on roads and for surveillance of remote locations</li>
<li>This can also be used as a traffic management system as on busy hours the traffic can be diverted to reduce rush on road.</li>
<li><p>By analysing the data the road utility can be calculated</p></li>
</ul>
<hr>
<h3>References</h3>
<a href="https://drive.google.com/file/d/1KC-jWD1DmnMOGtjkZs6clnlDGfUiZf5t/view">Theory</a>
