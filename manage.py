from app import create_app
from flask_script import Server,Manager

app = create_app('development')
@manager.Command
def test():
    '''Run the unittest tests.'''
    import unittest
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)
    
if __name__ == '__main__':
    manager.run()