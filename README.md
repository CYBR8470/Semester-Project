# Project Summary
To fit the 4-5 week development timeline, our team decided to develop an online game of Yahtzee. It is a familiar game with an established rule set and object parameters. We will work to codify it in the context of a server that controls dice values, rule sets, and scoring, a game-hosting client, and game-joining clients. We felt this design would help us to provide clear examples of some of the concepts developed during the course. 

## Installation
Installing and running the yahtzee application locally requires some terminal use to get started.

### Required Software
In order to run the yahtzee application locally, you must have Docker and Docker-Compose installed on your local machine.
Once you have Docker and a local copy of the repository installed, open a terminal window within the "project" folder, and then run the following command:
```bash
docker-compose build
```
After the project builds and is deployed locally, you should see text in the terminal window that says "Starting development server at http://0.0.0.0:8000/".
Once that appears, navigate to "http://localhost:8000" in your browser of choice to see the app running locally on your machine.

## Getting Started
TBD


# License
MIT License

Copyright (c) [2021] [Andrew Bullock and Pat Peters]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
