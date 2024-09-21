from array import array
import random
# The constructor is called to create the array.
valueList = array('f', [100, 3,4,5,6,8,1,4] )
# Fill the array with random floating-point values.
for i in range( len( valueList ) ) :
	valueList[ i ] = random.random()
# Print the values, one per line.
for value in valueList :
	print( value )
