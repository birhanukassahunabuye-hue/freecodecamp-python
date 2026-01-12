class SocialMediaProfile:
    def __init__(self, username, password):
        self.username = username
        self.passowrd = password
        self.is_logged_in = False
        self.is_private = True
        self.followers = []
        self.posts = []
    def login(self, entered_username, entered_password):
        if entered_username == self.username and entered_password == self.password:
            self.is_logged_in = True
        else:
            print("Incorrect input, Please! Try again!")

    def create_post(self, post):
        if self.is_logged_in == True:
            self.posts.append(post)
        else:
            print("please login to your account first!")


    def add_follower(self, profile_name):
        self.followers.append(profile_name)
    def view_profile(self):
        if self.is_logged_in ==True or self.is_private==False:
            for post in self.posts:
                print(post)
        else:
            print('This account is private.')




my_profile = SocialMediaProfile('@bire123', 1234321)
my_profile.login('bire12', 1234567)
my_profile.login('bire123', 1234321)
my_profile.create_post('Happy christmas my family!')
my_profile.create_post('Happy timket!')
my_profile.create_post('Eid Mubarek!')
my_profile.add_follower('user123')
my_profile.add_follower('user12')
my_profile.add_follower('user1234')
my_profile.add_follower('user1')
my_profile.view_profile()