# wizfi360-EVB-Pico_micropython
This project is for wizfi360-EVB-Pico

- [wizfi360-EVB-Pico_micropython](#wizfi360-evb-pico_micropython)

## Used verision of micropython
 - [v1.19.1(2022-06-18).uf2](https://micropython.org/resources/firmware/W5100S_EVB_PICO-20220618-v1.19.1.uf2)
![image](https://user-images.githubusercontent.com/9648281/182971266-8d43472b-c4fc-490b-a319-b0d61a716668.png)

# Getting Started

## Development environment configuration



> To test the ethernet examples, the development environment must be configured to use Raspberry Pi Pico. 

- Required development environment
   - [Thonny](https://thonny.org/) (that makes it easier to use micropython) 


1. First, import the library of the function you want to use from the uf2 file(PC) to your board. To uploading a file to using Thonny IDE, follow these next steps.
   
![1](https://user-images.githubusercontent.com/9648281/194994507-58bb17fd-8245-4fec-806a-a89d6bfc1f04.JPG)

2. Select httpParser.py and wizfi360.py among your PC files, right-click and select "upload to /".      

![2](https://user-images.githubusercontent.com/9648281/194994514-e7478425-6b2d-4cac-b096-33dcaf1ecc43.jpg)


3. You can see it like the picture below.

![3](https://user-images.githubusercontent.com/9648281/194994523-df454c50-b60c-4927-8d1f-86b830122c1f.JPG)
![4](https://user-images.githubusercontent.com/9648281/194995742-575d1f27-8d0a-4516-8e67-c57c9da2aba4.JPG)

4. If you upload the main.py on the board and the Run button is pressed, the main.py code in the board automatically runs.   

![5](https://user-images.githubusercontent.com/9648281/194996161-464c8e73-e8c5-4dc2-b7f1-3425b6583b85.JPG)


## Example
  ### 1. HTTP  :  [example > HTTP](./examples/HTTP)
  ### 2. TCP Client  :  [example > TCP Client](./examples/TCP%20Client)
  ### 3. UDP  :  [example > UDP](./examples/UDP)
