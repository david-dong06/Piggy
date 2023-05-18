#!/usr/bin python3
from teacher import PiggyParent
import sys
import time

class Piggy(PiggyParent):

    '''
    *************
    SYSTEM SETUP
    *************
    '''

    def __init__(self, addr=8, detect=True):
        PiggyParent.__init__(self) # run the parent constructor

        ''' 
        MAGIC NUMBERS <-- where we hard-code our settings
        '''
        self.LEFT_DEFAULT = 78
        self.RIGHT_DEFAULT = 80
        self.MIDPOINT = 1500  # what servo command (1000-2000) is straight forward for your bot?
        self.set_motor_power(self.MOTOR_LEFT + self.MOTOR_RIGHT, 0)
        self.load_defaults()
        
    def load_defaults(self):
        """Implements the magic numbers defined in constructor"""
        self.set_motor_limits(self.MOTOR_LEFT, self.LEFT_DEFAULT)
        self.set_motor_limits(self.MOTOR_RIGHT, self.RIGHT_DEFAULT)
        self.set_servo(self.SERVO_1, self.MIDPOINT)
        
    def menu(self):
        """Displays menu dictionary, takes key-input and calls method"""
        ## This is a DICTIONARY, it's a list with custom index values. Python is cool.
        # Please feel free to change the menu and add options.
        print("\n *** MENU ***") 
        menu = {"n": ("Navigate", self.nav),
                "d": ("Dance", self.dance),
                "o": ("Obstacle count", self.obstacle_count),
                "s": ("Shy", self.shy),
                "f": ("Follow", self.follow),
                "c": ("Calibrate", self.calibrate),
                "q": ("Quit", self.quit),
                "z": ("David", self.david),
                "v": ("move_servo", self.servo),
                "m": ("Maze", self.maze),
                "e": ("Dodge", self.dodge),
                "p": ("stop", self.pots),
                "a": ("Avoid", self.avoid)
                }
        # loop and print the menu...
        for key in sorted(menu.keys()):
            print(key + ":" + menu[key][0])
        # store the user's answer
        ans = str.lower(input("Your selection: "))
        # activate the item selected
        menu.get(ans, [None, self.quit])[1]()

    '''
    ****************
    STUDENT PROJECTS
    ****************
    '''
    def move_servo(self):
      self.servo(1000)
    '''
    def avoid(self):
      self.servo(1500)
      self.turn_to_deg(0)
      if self.read_distance()<=100:
        return False
      return True
      if True:
        for side in range(10):
          self.deg_fwd(1080)
      if False:
        self.turn_to_deg(90)
        self.servo(1000)
      if self.read_distance()<=200
    '''

    def avoid(self):
      while True:
        if self.detect() is True:
          self.deg_fwd(360)
        if self.detect() is false:
          self.turn_by_deg(86)
          self.stop()
          self.deg_fwd(720)
          self.stop()
          self.turn_by_deg(-86)
          self.stop()
          self.deg_by_deg(1080)
                      
        
      
    def detect(self):
      if self.read_distance()<=100:
        return False
      return True 

    def maze(self):
      while True:
        if self.detect() is False:
          self.stop()
          self.turn_by_deg(85)
          if self.detect() is False:
            self.turn_by_deg(-175)
            self.stop()
        else:
          self.deg_fwd(360)
        
    def dodge(self):
      while True:
        if self.detect() is True:
          self.deg_fwd(360)
        if self.detect() is False:
          self.turn_by_deg(172)
          self.stop()
          self.fwd()
          time.sleep(3)
          self.turn_by_deg(172)
          self.stop()
         
    def pots(self):
      while True:
        if self.detect() is True:
          self.deg_fwd(360)
        if self.detect() is False:
          self.stop()
        
        
  
    def david(self):
      print("this is for testing")
      for side in range(4):
        self.fwd()
        time.sleep(1)
        self.turn_by_deg(90)
    
      
      
    def safe_to_dance(self):
      
        for x in range(10):
          
          self.turn_by_deg(36)
          if self.read_distance()<=100:
            return False
        return True
            
    def dance(self):
      if self.safe_to_dance() == False:
        self.stop()
      else:
        self.right()
        time.sleep(2)
        self.left()
        time.sleep(2)
        self.right()
        time.sleep(3)
        self.left()
        time.sleep(3)
        self.deg_fwd(360)
        self.back()
        time.sleep(2)
        self.stop()
     

    def shake(self):
        """ Another example move """
        self.deg_fwd(720)
        self.stop()

    def example_move(self):
        """this is an example dance move that should be replaced by student-created content"""
        self.right() # start rotating right
        time.sleep(1) # turn for a second
        self.stop() # stop
        self.servo(1000) # look right
        time.sleep(.25) # give your head time to move
        self.servo(2000) # look left

    def scan(self):
        """Sweep the servo and populate the scan_data dictionary"""
        for angle in range(self.MIDPOINT-350, self.MIDPOINT+350, 3):
            self.servo(angle)
            self.scan_data[angle] = self.read_distance()

    def obstacle_count(self):
        """Does a 360 scan and returns the number of obstacles it sees"""
        pass

    def nav(self):
        print("-----------! NAVIGATION ACTIVATED !------------\n")
        print("-------- [ Press CTRL + C to stop me ] --------\n")
        print("-----------! NAVIGATION ACTIVATED !------------\n")
        
        # TODO: build self.quick_check() that does a fast, 3-part check instead of read_distance
        while self.read_distance() > 250:  # TODO: fix this magic number
            self.fwd()
            time.sleep(.01)
        self.stop()
        # TODO: scan so we can decide left or right
        # TODO: average the right side of the scan dict
        # TODO: average the left side of the scan dict
        


###########
## MAIN APP
if __name__ == "__main__":  # only run this loop if this is the main file

    p = Piggy()

    if sys.version_info < (3, 0):
        sys.stdout.write("Sorry, requires Python 3.x\n")
        p.quit()

    try:
        while True:  # app loop
            p.menu()

    except KeyboardInterrupt: # except the program gets interrupted by Ctrl+C on the keyboard.
        p.quit()  
