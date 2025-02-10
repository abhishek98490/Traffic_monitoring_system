# Traffic Monitoring System  (In Progress)

This project aims to fetch traffic camera images from the Singapore Land Transport Authority (LTA) OneMotoring website, classify different vehicle types (such as cars, buses, two-wheelers, etc.), and track real-time traffic conditions. The goal is to create a solution that can process traffic camera feeds, display the results on a dashboard, and provide real-time insights to end-users.

## Features (Work In Progress)

- **Fetching Traffic Camera Images**: Currently implementing image scraping from OneMotoring's website.
- **Vehicle Classification**: Implementing a vehicle classification system (car, bus, two-wheeler, etc.) using machine learning models.
- **Dashboard**: Developing a real-time dashboard to visualize the results (vehicle counts, traffic status).
- **Periodic Updates**: Fetching and processing new images periodically (still under development).

## Current Status

### 1. **Data Fetching**:
- Fetching traffic camera images for a specific location is implemented.
- Working on dynamically switching between different traffic camera locations.

### 2. **Vehicle Classification**:
- The vehicle classification component is under development. Integration with pre-trained machine learning models like YOLO or SSD is being planned.
- Currently, focusing on testing basic models and preprocessing steps.

### 3. **Real-time Dashboard**:
- **To be implemented**: Developing a simple dashboard (using libraries like Streamlit, Flask, or Dash) to show the real-time data.
- **Current Status**: Working on fetching images and displaying them for testing purposes.
