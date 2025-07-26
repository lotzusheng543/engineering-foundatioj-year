import math 

class equations:
    def __init__(self, flow_speed, river_width, speed_of_boat, Direction_of_boat, y ):# collecting all the datas from the controls 
        self.flow_speed = flow_speed
        self.river_width = river_width
        self.speed_of_boat = speed_of_boat
        self.direction_of_boat = Direction_of_boat
        self.y = y * 0.5



    def actual_velocity(self):
        self.a_velocity = math.sqrt((self.flow_speed**2) + (self.speed_of_boat**2) - 2*self.flow_speed*self.speed_of_boat*math.cos(math.radians(self.direction_of_boat+90)))
        return self.a_velocity
    
    def actual_angle(self):
        #print(self.speed_of_boat * math.sin(-math.radians(self.direction_of_boat)))
        if self.flow_speed == 0:#temporary solution
            self.a_angle = abs(-90 + self.direction_of_boat)
            return self.a_angle
        elif self.direction_of_boat < 0 and self.speed_of_boat * math.sin(-math.radians(self.direction_of_boat)) > self.flow_speed:
            self.a_angle = 180 - math.degrees(math.asin((self.speed_of_boat/self.a_velocity) * math.sin(math.radians(self.direction_of_boat+ 90 ))))
            #print('1')
            return self.a_angle
        elif self.direction_of_boat < 0 and self.speed_of_boat * math.sin(-math.radians(self.direction_of_boat)) < self.flow_speed:
            self.a_angle = math.degrees(math.asin((self.speed_of_boat/self.a_velocity) * math.sin(math.radians(self.direction_of_boat+ 90 ))))
            #print('2')
            return self.a_angle

        elif self.direction_of_boat < 0 and self.speed_of_boat * math.sin(-math.radians(self.direction_of_boat)) == self.flow_speed:
            self.a_angle = abs(-90 + self.direction_of_boat)
            #print('3')
            return self.a_angle
        else :
            self.a_angle = math.degrees(math.asin((self.speed_of_boat/self.a_velocity) * math.sin(math.radians(self.direction_of_boat+ 90 ))))
            return self.a_angle

    def time(self):
        self.time_t = self.river_width/(self.a_velocity * math.sin(math.radians(self.a_angle)))
        return self.time_t
    
    def vertical_distance(self ):

        self.v_distance =  self.river_width/math.tan(math.radians(self.a_angle)) + self.y
        #self.a_velocity * math.cos(math.radians(self.a_angle)) * self.time_t
        #print(self.v_distance)
        return self.v_distance

    def challenge_check(self, challenge_point):
        #self.vertical_distance = self.river_width/math.tan(math.radians(self.a_angle))
        #check if it's within a range so it is easier for the user to pass the game
        #print(challenge_point, self.v_distance)
        if challenge_point-10<= self.v_distance <= challenge_point+10:
            return True
        else:
            return False
        
    def horizontal_distance(self, x):
        self.startx = x * 0.5
        self.h_distance = self.startx + self.river_width * (x/800) + 50 * (x/800)
        return self.h_distance

         


