#look at the growth of nested dictionaries

import numpy as np
from memory_profiler import profile

@profile
def example():
    #100 key values
    Dict_one = {'Blake': 19,
                'Michael': 22,
                'John': 20,
                'Kelly': 22,
                'Jack': 21,
                'David': 20,
                'Blake': 19,
                'Michael': 22,
                'John': 20,
                'Kelly': 22,
                'Jack': 21,
                'David': 20,
                'Blake': 19,
                'Michael': 22,
                'John': 20,
                'Kelly': 22,
                'Jack': 21,
                'David': 20,
                'Blake': 19,
                'Michael': 22,
                'John': 20,
                'Kelly': 22,
                'Jack': 21,
                'David': 20,
                'Blake': 19,
                'Michael': 22,
                'John': 20,
                'Kelly': 22,
                'Jack': 21,
                'David': 20,
                'Blake': 19,
                'Michael': 22,
                'John': 20,
                'Kelly': 22,
                'Jack': 21,
                'David': 20,
                'Blake': 19,
                'Michael': 22,
                'John': 20,
                'Kelly': 22,
                'Jack': 21,
                'David': 20,
                'Blake': 19,
                'Michael': 22,
                'John': 20,
                'Kelly': 22,
                'Jack': 21,
                'David': 20,
                'Blake': 19,
                'Michael': 22,
                'John': 20,
                'Kelly': 22,
                'Jack': 21,
                'David': 20,
                'Blake': 19,
                'Michael': 22,
                'John': 20,
                'Kelly': 22,
                'Jack': 21,
                'David': 20,
                'Blake': 19,
                'Michael': 22,
                'John': 20,
                'Kelly': 22,
                'Jack': 21,
                'David': 20,
                'Blake': 19,
                'Michael': 22,
                'John': 20,
                'Kelly': 22,
                'Jack': 21,
                'David': 20,
                'Blake': 19,
                'Michael': 22,
                'John': 20,
                'Kelly': 22,
                'Jack': 21,
                'David': 20,
                'Blake': 19,
                'Michael': 22,
                'John': 20,
                'Kelly': 22,
                'Jack': 21,
                'David': 20,
                'Blake': 19,
                'Michael': 22,
                'John': 20,
                'Kelly': 22,
                'Jack': 21,
                'David': 20,
                'Blake': 19,
                'Michael': 22,
                'John': 20,
                'Kelly': 22,
                'Jack': 21,
                'David': 20,
                'Blake': 19,
                'Michael': 22,
                'John': 20,
                'Kelly': 22,
                'Jack': 21}
    
    #{1 key value: {100 key values}}
    Dict_two = {'nest' : {
                'Blake': 19,
                'Michael': 22,
                'John': 20,
                'Kelly': 22,
                'Jack': 21,
                'David': 20,
                'Blake': 19,
                'Michael': 22,
                'John': 20,
                'Kelly': 22,
                'Jack': 21,
                'David': 20,
                'Blake': 19,
                'Michael': 22,
                'John': 20,
                'Kelly': 22,
                'Jack': 21,
                'David': 20,
                'Blake': 19,
                'Michael': 22,
                'John': 20,
                'Kelly': 22,
                'Jack': 21,
                'David': 20,
                'Blake': 19,
                'Michael': 22,
                'John': 20,
                'Kelly': 22,
                'Jack': 21,
                'David': 20,
                'Blake': 19,
                'Michael': 22,
                'John': 20,
                'Kelly': 22,
                'Jack': 21,
                'David': 20,
                'Blake': 19,
                'Michael': 22,
                'John': 20,
                'Kelly': 22,
                'Jack': 21,
                'David': 20,
                'Blake': 19,
                'Michael': 22,
                'John': 20,
                'Kelly': 22,
                'Jack': 21,
                'David': 20,
                'Blake': 19,
                'Michael': 22,
                'John': 20,
                'Kelly': 22,
                'Jack': 21,
                'David': 20,
                'Blake': 19,
                'Michael': 22,
                'John': 20,
                'Kelly': 22,
                'Jack': 21,
                'David': 20,
                'Blake': 19,
                'Michael': 22,
                'John': 20,
                'Kelly': 22,
                'Jack': 21,
                'David': 20,
                'Blake': 19,
                'Michael': 22,
                'John': 20,
                'Kelly': 22,
                'Jack': 21,
                'David': 20,
                'Blake': 19,
                'Michael': 22,
                'John': 20,
                'Kelly': 22,
                'Jack': 21,
                'David': 20,
                'Blake': 19,
                'Michael': 22,
                'John': 20,
                'Kelly': 22,
                'Jack': 21,
                'David': 20,
                'Blake': 19,
                'Michael': 22,
                'John': 20,
                'Kelly': 22,
                'Jack': 21,
                'David': 20,
                'Blake': 19,
                'Michael': 22,
                'John': 20,
                'Kelly': 22,
                'Jack': 21,
                'David': 20,
                'Blake': 19,
                'Michael': 22,
                'John': 20,
                'Kelly': 22,
                'Jack': 21}
                } 

    # {1 key value: {1 key value : {100 key values}}}
    dict_three = {'nest' : {'nest': {
                'Blake': 19,
                'Michael': 22,
                'John': 20,
                'Kelly': 22,
                'Jack': 21,
                'David': 20,
                'Blake': 19,
                'Michael': 22,
                'John': 20,
                'Kelly': 22,
                'Jack': 21,
                'David': 20,
                'Blake': 19,
                'Michael': 22,
                'John': 20,
                'Kelly': 22,
                'Jack': 21,
                'David': 20,
                'Blake': 19,
                'Michael': 22,
                'John': 20,
                'Kelly': 22,
                'Jack': 21,
                'David': 20,
                'Blake': 19,
                'Michael': 22,
                'John': 20,
                'Kelly': 22,
                'Jack': 21,
                'David': 20,
                'Blake': 19,
                'Michael': 22,
                'John': 20,
                'Kelly': 22,
                'Jack': 21,
                'David': 20,
                'Blake': 19,
                'Michael': 22,
                'John': 20,
                'Kelly': 22,
                'Jack': 21,
                'David': 20,
                'Blake': 19,
                'Michael': 22,
                'John': 20,
                'Kelly': 22,
                'Jack': 21,
                'David': 20,
                'Blake': 19,
                'Michael': 22,
                'John': 20,
                'Kelly': 22,
                'Jack': 21,
                'David': 20,
                'Blake': 19,
                'Michael': 22,
                'John': 20,
                'Kelly': 22,
                'Jack': 21,
                'David': 20,
                'Blake': 19,
                'Michael': 22,
                'John': 20,
                'Kelly': 22,
                'Jack': 21,
                'David': 20,
                'Blake': 19,
                'Michael': 22,
                'John': 20,
                'Kelly': 22,
                'Jack': 21,
                'David': 20,
                'Blake': 19,
                'Michael': 22,
                'John': 20,
                'Kelly': 22,
                'Jack': 21,
                'David': 20,
                'Blake': 19,
                'Michael': 22,
                'John': 20,
                'Kelly': 22,
                'Jack': 21,
                'David': 20,
                'Blake': 19,
                'Michael': 22,
                'John': 20,
                'Kelly': 22,
                'Jack': 21,
                'David': 20,
                'Blake': 19,
                'Michael': 22,
                'John': 20,
                'Kelly': 22,
                'Jack': 21,
                'David': 20,
                'Blake': 19,
                'Michael': 22,
                'John': 20,
                'Kelly': 22,
                'Jack': 21}
                }
              }
    
    # {1 key value: {1 key value : {1 key value : {100 key values}}}}
    dict_four = {'nest' : {'nest': {
                'nest': {
                'Blake': 19,
                'Michael': 22,
                'John': 20,
                'Kelly': 22,
                'Jack': 21,
                'David': 20,
                'Blake': 19,
                'Michael': 22,
                'John': 20,
                'Kelly': 22,
                'Jack': 21,
                'David': 20,
                'Blake': 19,
                'Michael': 22,
                'John': 20,
                'Kelly': 22,
                'Jack': 21,
                'David': 20,
                'Blake': 19,
                'Michael': 22,
                'John': 20,
                'Kelly': 22,
                'Jack': 21,
                'David': 20,
                'Blake': 19,
                'Michael': 22,
                'John': 20,
                'Kelly': 22,
                'Jack': 21,
                'David': 20,
                'Blake': 19,
                'Michael': 22,
                'John': 20,
                'Kelly': 22,
                'Jack': 21,
                'David': 20,
                'Blake': 19,
                'Michael': 22,
                'John': 20,
                'Kelly': 22,
                'Jack': 21,
                'David': 20,
                'Blake': 19,
                'Michael': 22,
                'John': 20,
                'Kelly': 22,
                'Jack': 21,
                'David': 20,
                'Blake': 19,
                'Michael': 22,
                'John': 20,
                'Kelly': 22,
                'Jack': 21,
                'David': 20,
                'Blake': 19,
                'Michael': 22,
                'John': 20,
                'Kelly': 22,
                'Jack': 21,
                'David': 20,
                'Blake': 19,
                'Michael': 22,
                'John': 20,
                'Kelly': 22,
                'Jack': 21,
                'David': 20,
                'Blake': 19,
                'Michael': 22,
                'John': 20,
                'Kelly': 22,
                'Jack': 21,
                'David': 20,
                'Blake': 19,
                'Michael': 22,
                'John': 20,
                'Kelly': 22,
                'Jack': 21,
                'David': 20,
                'Blake': 19,
                'Michael': 22,
                'John': 20,
                'Kelly': 22,
                'Jack': 21,
                'David': 20,
                'Blake': 19,
                'Michael': 22,
                'John': 20,
                'Kelly': 22,
                'Jack': 21,
                'David': 20,
                'Blake': 19,
                'Michael': 22,
                'John': 20,
                'Kelly': 22,
                'Jack': 21,
                'David': 20,
                'Blake': 19,
                'Michael': 22,
                'John': 20,
                'Kelly': 22,
                'Jack': 21}}}}
    
    # {1 key value: {1 key value : {1 key value : {1 key value : {100 key values}}}}}
    dict_five = {'nest' : {'nest': {
                'nest': { 'nest': {
                'Blake': 19,
                'Michael': 22,
                'John': 20,
                'Kelly': 22,
                'Jack': 21,
                'David': 20,
                'Blake': 19,
                'Michael': 22,
                'John': 20,
                'Kelly': 22,
                'Jack': 21,
                'David': 20,
                'Blake': 19,
                'Michael': 22,
                'John': 20,
                'Kelly': 22,
                'Jack': 21,
                'David': 20,
                'Blake': 19,
                'Michael': 22,
                'John': 20,
                'Kelly': 22,
                'Jack': 21,
                'David': 20,
                'Blake': 19,
                'Michael': 22,
                'John': 20,
                'Kelly': 22,
                'Jack': 21,
                'David': 20,
                'Blake': 19,
                'Michael': 22,
                'John': 20,
                'Kelly': 22,
                'Jack': 21,
                'David': 20,
                'Blake': 19,
                'Michael': 22,
                'John': 20,
                'Kelly': 22,
                'Jack': 21,
                'David': 20,
                'Blake': 19,
                'Michael': 22,
                'John': 20,
                'Kelly': 22,
                'Jack': 21,
                'David': 20,
                'Blake': 19,
                'Michael': 22,
                'John': 20,
                'Kelly': 22,
                'Jack': 21,
                'David': 20,
                'Blake': 19,
                'Michael': 22,
                'John': 20,
                'Kelly': 22,
                'Jack': 21,
                'David': 20,
                'Blake': 19,
                'Michael': 22,
                'John': 20,
                'Kelly': 22,
                'Jack': 21,
                'David': 20,
                'Blake': 19,
                'Michael': 22,
                'John': 20,
                'Kelly': 22,
                'Jack': 21,
                'David': 20,
                'Blake': 19,
                'Michael': 22,
                'John': 20,
                'Kelly': 22,
                'Jack': 21,
                'David': 20,
                'Blake': 19,
                'Michael': 22,
                'John': 20,
                'Kelly': 22,
                'Jack': 21,
                'David': 20,
                'Blake': 19,
                'Michael': 22,
                'John': 20,
                'Kelly': 22,
                'Jack': 21,
                'David': 20,
                'Blake': 19,
                'Michael': 22,
                'John': 20,
                'Kelly': 22,
                'Jack': 21,
                'David': 20,
                'Blake': 19,
                'Michael': 22,
                'John': 20,
                'Kelly': 22,
                'Jack': 21}}}}}
    
    # {1 key value: {1 key value : {1 key value : {1 key value : {1 key value : {100 key values}}}}}}
    dict_six = {'nest' : {'nest': {
                'nest': { 'nest': { 'nest': {
                'Blake': 19,
                'Michael': 22,
                'John': 20,
                'Kelly': 22,
                'Jack': 21,
                'David': 20,
                'Blake': 19,
                'Michael': 22,
                'John': 20,
                'Kelly': 22,
                'Jack': 21,
                'David': 20,
                'Blake': 19,
                'Michael': 22,
                'John': 20,
                'Kelly': 22,
                'Jack': 21,
                'David': 20,
                'Blake': 19,
                'Michael': 22,
                'John': 20,
                'Kelly': 22,
                'Jack': 21,
                'David': 20,
                'Blake': 19,
                'Michael': 22,
                'John': 20,
                'Kelly': 22,
                'Jack': 21,
                'David': 20,
                'Blake': 19,
                'Michael': 22,
                'John': 20,
                'Kelly': 22,
                'Jack': 21,
                'David': 20,
                'Blake': 19,
                'Michael': 22,
                'John': 20,
                'Kelly': 22,
                'Jack': 21,
                'David': 20,
                'Blake': 19,
                'Michael': 22,
                'John': 20,
                'Kelly': 22,
                'Jack': 21,
                'David': 20,
                'Blake': 19,
                'Michael': 22,
                'John': 20,
                'Kelly': 22,
                'Jack': 21,
                'David': 20,
                'Blake': 19,
                'Michael': 22,
                'John': 20,
                'Kelly': 22,
                'Jack': 21,
                'David': 20,
                'Blake': 19,
                'Michael': 22,
                'John': 20,
                'Kelly': 22,
                'Jack': 21,
                'David': 20,
                'Blake': 19,
                'Michael': 22,
                'John': 20,
                'Kelly': 22,
                'Jack': 21,
                'David': 20,
                'Blake': 19,
                'Michael': 22,
                'John': 20,
                'Kelly': 22,
                'Jack': 21,
                'David': 20,
                'Blake': 19,
                'Michael': 22,
                'John': 20,
                'Kelly': 22,
                'Jack': 21,
                'David': 20,
                'Blake': 19,
                'Michael': 22,
                'John': 20,
                'Kelly': 22,
                'Jack': 21,
                'David': 20,
                'Blake': 19,
                'Michael': 22,
                'John': 20,
                'Kelly': 22,
                'Jack': 21,
                'David': 20,
                'Blake': 19,
                'Michael': 22,
                'John': 20,
                'Kelly': 22,
                'Jack': 21}}}}}}

if __name__ == '__main__':
    example()
