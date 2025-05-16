def factorial(x: int) -> int:
    a = 1
    for i in range(1,x+1):
        a*=i
    return a


def numerize(x: any) -> any:
    """
    returns string input in integer type if possible
        if not then in float type
        if not that then just left as is

        notice: does not work with complex due to the ambguitiy of the presence of j
    """
    #example cases:
    """
    '2.000000'
    '2.0'
    '2'
    2.0000
    2.0
    2
    """
    try:
        x = float(x)
    except:
        return x #if it cant even be converted to a float then it aint numeric
    if int(x) == float(x):
        return int(x)
    else:
        return float(x)
        

def pi_reducer(x) -> float:
    pi = 3.1415926535 #approx
    while x >= 2*pi:
        x-=2*pi
    return x

def sine(x,n=50) -> float:
    ## at approximately 8 digit accuracy rn
    x = pi_reducer(x)
    index = 3
    sign = -1 #1 = postive, -1 = negative
    result = x
    for _ in range(n):
        exponent = x**index
        expression = exponent/factorial(index)
        final_expression = sign * expression
        result += final_expression
        #next iteration config
        index += 2
        sign *= -1
    return result

def cosecant(x,n=50) -> float:
    return (1/sine(x,n))

def sine_method_for_pi(accuracy=10000) -> float:
    radian_converter = (3.14159265359/180) # we need pi for the radian conversion, ik its a bit circular reasoning
    degree_input = (180/accuracy) * radian_converter
    return (accuracy * sine(degree_input))
def arctan(x,n=1000000) -> float:
    #approx 6-7 digit accuracy
    if not (-1<=x<=1):
        """
        use co function  identity:
        arctan (x) = pi/2 - arctan(1/x)

        to reduce x value to fit valid convergence domain
        """
        pi = 3.1415926535
        try:
            return (pi/2 - arctan(1/x))
        except:
            raise(ValueError("Invalid dominan: arctan input is between -1 and 1"))
    index = 3
    sign = -1 #1 = postive, -1 = negative
    result = x
    match x:
        case -1:
            for _ in range(n):
                expression = -1/index
                final_expression = sign * expression
                result += final_expression
                #next iteration config
                index += 2
                sign *= -1
        case 1:
            for _ in range(n):
                expression = 1/index
                final_expression = sign * expression
                result += final_expression
                #next iteration config
                index += 2
                sign *= -1
        case _:
            for _ in range(n):
                exponent = x**index
                expression = exponent/index
                final_expression = sign * expression
                result += final_expression
                #next iteration config
                index += 2
                sign *= -1

    
    return result

def arctan_method_for_pi(n=1000000) -> float:
    #default output: 3.1415936535887745
    return (arctan(1,n) * 4)
    # 6 digits from 100,000
    # 8 digits from 500 million

def approximate(x):
    return round(x,5)

def DerivitaveAtPoint(func,x,h=0.000000001) -> float:
    return (func(x+h) - func(x))/h


def golden_ratio(depth: int) -> float:
    #depth of 40 means 15 digit accuracy
    a = 0
    b = 1
    for _ in range(depth):
        a,b = b,a + b
    return b/a


def factors(x: int) -> list[list]: 
    results = []
    for i in range(1,round(x**0.5)+1):
        if x % i == 0:
            results.append([i,numerize(x/i)])
    return results


def isPrime(x: int) -> bool:
    if x <= 1:
        return False
    for i in range(2,round(x**0.5)+1):
        if x % i == 0:
            return False
    return True


def isComposite(x: int) -> bool:
    for i in range(2,round(x**0.5)+1):
        if x % i == 0:
            return True
    return False


def reimann_integral(func,lower_bound,upper_bound,h=0.00001) -> float:
    sum = 0
    negative_integral = False
    if lower_bound > upper_bound:
        lower_bound,upper_bound = upper_bound,lower_bound #swap if wrong order detected
        negative_integral = True #still accounts for negativity
    elif lower_bound == upper_bound:
        return 0
    while lower_bound < upper_bound:
        sum += (func(lower_bound)*h)
        lower_bound += h
    return sum if not negative_integral else -sum


def cosine(x,n=50) -> float:
    # approx 15-16 digit accuracy
    x = pi_reducer(x)
    index = 2
    sign = -1
    result = 1
    for _ in range(n):
        result += sign * (x**index)/factorial(index)
        index += 2
        sign *= -1
    return result

def tan(x,n=50) -> float:
    return (sine(x,n)/cosine(x,n))

def cot(x,n=50) -> float:
    return (cosine(x,n)/sine(x,n))

def secant(x,n=50) -> float:
    #approx 15 decimal digit accuracy
    return (1/cosine(x,n))

def combination(x,y):
    "formula = n! all divded by k! * (n-k)!"
    
    #example case: 10, 5
    if y == 0 or x==y:
        return 1
    if x>y:
        
        uncommon_products = range((1+(x-y)),x+1) # 10! -> 5! * 6 * 7 * 8 * 9 * 10
        uncommon_numerator = 1
        for i in uncommon_products:
            uncommon_numerator *= i
        return uncommon_numerator//factorial(y)
    else: #x<y
        raise ValueError("second term(y) cannot be more than first term(x)")

def arcsin(x,n=150):
    #around the edges is not recommended lol
    match x:
        case 1:
            return 1.570796326794896
        case -1:
            return -1.570796326794896
    if not (-1<=x<=1):
        raise(ValueError("Invalid dominan: arcsin input is between -1 and 1"))
    result = 0
    for i in range(n):
        comb = combination(2*i,i)
        denominator_1 = 4**i
        denominator_2 = (2*i + 1)
        denominator_3 = x**-(2*i + 1)
        denominator = denominator_1 * denominator_2 * denominator_3
        result += comb/denominator
    return result


def permutations(x,y):
    "formula = n! divded by (n-k)!"
    "we split n! into n-k! * (k*k+1*k+2...n)"
    "allowing us to cancel n-k on both sides, leaving us the product of all those uncommon factors"
    if y == 0 or x==y:
        return 1
    uncommon_products = range((1+(x-y)),x+1) # 10! -> 5! * 6 * 7 * 8 * 9 * 10
    uncommon_numerator = 1
    for i in uncommon_products:
        uncommon_numerator *= i
    return uncommon_numerator

def arccos(x,n=150):
    pi = 3.1415926535
    return (pi/2 - arcsin(x,n))

def e_exp_taylor(x,n=150):
    e = 2.718281828459045
    match x:
        case 0:
            return 1
        case 1:
            return e
    result = 0
    for i in range(n):
        result += (x**i)/(factorial(i))
    return result

def e_exp_eval(x):
    e = 2.7182818284590452353602
    return e**x



def eix(x,n=50):
    return (cosine(x,n) + sine(x,n)*1j)

def ln_taylor(x,n=200):
    """
    THIS IS A SUB FUNCTION. NOT TO BE USED ON ITS OWN
    """
    if x == 0:
        raise ZeroDivisionError("ln(0) is undefined")
    #configure input
    x  -= 1
    #initlaize vars
    result = x
    index = 2
    sign = -1
    for _ in range(n):
        exoponential = x**index
        divisor = 1/index # through reciprocal multiplication
        term = exoponential * divisor * sign
        result += term
        index += 1
        sign *= -1
    return result * 2 #cuz thats the identity

def ln_arctanh_taylor(x,n=200) -> float:
    """
    THIS IS A SUB FUNCTION. NOT TO BE USED ON ITS OWN

    best for 0.05 < x < 35

    no higher than 39
    no lower than 0.02

    its way worse if its too low
    """
    if x <= 0:
        raise ValueError("invalid domain for the arctanh definition on ln(x)")
    elif abs(x-1) < 1e-10: #checks if input is within 1e-10 of 1, then assumes the input is 1 if so
        return 0.0
    #configure input
    hyperbolic_x = (x-1)/(x+1)
    #check for bad inputs
    if abs(x) < 0.05 and abs(x-1) > 0.01:
        #check 1 ensures hyperbolic x isnt too close to zero
        #check 2 ensures x isn't too close to 1, cuz infinite rercursion on the reciproral would occur since 1**-1 = 1
        return -ln_arctanh_taylor(1/x) #my favorite log identity
    #initalize vdalues
    result = hyperbolic_x
    index = 3
    #factor = reciproocal of index
    for _ in range(n):
        exponentiation = hyperbolic_x**index
        reciprocal_factor = 1/index # not index**-1 cuz 1/index is slightly faster
        final_term = reciprocal_factor * exponentiation
        result += final_term
        #next iter config
        index += 2
    return result * 2



def ln(x,n=200) -> float:
    """
    computes natural log of x using arctanh taylor series and a log expansion algoithim


    you dont have to worry about extreme small/large values being inaccurate
    the only limit is your CPU
    """

    def ln_expansion(x: list) -> list:
        """
        expected input is a list of ints/floats that of which are all less than 2
        EXCEPT the last one which will be reduced by adding another terms into the list
            so heres a full case of the expansion algorithim:
        ln(5) -> ln(5) is selected because 5-1 > 1
        ln(5/4) + ln(4)
        ln(5/4) + ln(4/3) + ln(3)
        ln(5/4) + ln(4/3) + ln(3/2) + ln(2)
        ln(5/4) + ln(4/3) + ln(3/2) + ln(2)
        ln(2),the end case, will be customly converted into ln(9/8) + 2ln(4/3)
        """
        while x[-1] > 2:
            divsor = x[-1] - 1
            x.append(divsor)
            x[-2] = (x[-2])/divsor
        x.pop(-1)
        x.append(9/8)
        x.append(4/3)
        x.append(4/3)
        #that part replaces the base case of ln(2) with ln(9/8) + 2ln(4/3)
        return x
    ln_sum = []
    x = numerize(x)
    match x:
        case float():
            if abs(x) > 2:
                a = x//2
                b = a*2
                c = x/b
                ln_sum = [c,b] #initial sequence
                ln_sum = ln_expansion(ln_sum) #sequence continuation
            else: # |x| < 2
                if 1/x >= 2: #aka X <= 1/2
                    return -ln(1/x)
                else: # x is more than one half
                    #multiply by 4 to ensure x is at least 2
                    #then we apply correspondinglog property by subtracting by ln(4)
                    return ln(x*4) - ln(4)
        case int():
            match x:
                case 0:
                    raise ZeroDivisionError("ln(0) is undefined")
                case 1:
                    return 0.0
            #base cases 0,1 are handled
            if x != 2: #only applies for non base case
                a = x//2
                b = a*2
                c = x/b
                ln_sum = [c,b] #initial sequence
            else: #base case 2 fallback
                ln_sum = [2] #initial sequence (not thats theres much to continnue)
            ln_sum = ln_expansion(ln_sum) #sequence continuation
        case complex():
            complex_info = polar_form(x,1)
            modulus = complex_info[0]
            theta = complex_info[1]
            return [ln(modulus),ln(theta) * 1j]
        case _:
            raise TypeError(f"invalid input: {x}")
    #ln evaluation time
    evaluated_list = [ln_arctanh_taylor(i,n) for i in ln_sum]
    answer = sum(evaluated_list)
    if abs(answer-1) < 1e-13:
        return 1.0
    else:
        return answer

def polar_form(x: complex,output_type = 1):
    """
    Returns polar form of given complex number

    Input types:
    1. Returns list containing both variables
    ex: [5,0.927] - this means the modulus = 5 and theta is approx 0.927
    
    2. Returns literal string that can be mathematically evaluated
    ex: 5*(e**(0.927j)) as filled: r*e^(i*theta)
    """
    #first find modulus(abs value) of complex number
    #yes im aware its a built in feature but thats no fun

    modulus = ((x.imag)**2 + (x.real)**2)**0.5
    modulus = numerize(modulus)

    theta = arctan(x.imag/x.real) * 1j
    theta = numerize(theta)

    match output_type:
        case 1: # string output
            return f"{modulus}*(e**({theta}))"
        case 2: # list output
            return [modulus,theta]
        case _:
            raise ValueError("invalid output type")


def a_root(x,a=2,n=200):
    match x<0:
        case True:
            result = e_exp_eval(ln(-x,n)/a)
            validated_result = validate_round(result)
            if validate_round(result**a) == -x:
                return result * 1j
            else:
                return validated_result * 1j
        case False:
            result = e_exp_eval(ln(x,n)/a)
            validated_result = validate_round(result)
            if validate_round(result**a) == x:
                return result
            else:
                return validated_result


def validate_round(actual,SENSITIVITY=4) -> float:
    """
    input a number to be approximated if possible by leading 9's or 0's(sensitivity arg)
    intended for usage to detect floating point errors

    """
    if isinstance(actual,complex):
        return complex(real=validate_round(actual.real),imag=(validate_round(actual.imag)))
    #attempt round down
    floor = int(actual)
    if actual - floor < (10**-(SENSITIVITY+1)):
        return floor
    
    #attempt round up
    ceiling = int(actual + 1)
    if ceiling - actual < (10**-(SENSITIVITY+1)):
        return ceiling
    
    # floating 9s check

    str_list = list(reversed(str(actual)))
    counter = 0 #counts current amount of nines
    for i in range(len(str_list)):
        if str_list[i] == "9":
          counter += 1
        else:
            if counter > SENSITIVITY and str_list[i] != ".":
                str_list[i] = str(int(str_list[i]) + 1)
                for j in range(i):
                    str_list[j] = "0" if str_list[j] != "." else "." #this if statement prevents the period from being replaced with a zero
            counter = counter if str_list[i] == "." else 0
    result = "".join(reversed(str_list))
    result = numerize(result)

    # floating zeros check

    str_list = list(str(result))
    try:
        start = str_list.index(".")
    except:
        return result #if its not a decimal then theres no float to check
    counter = 0
    for i in range(start,len(str_list)):
        if str_list[i] == "0":
            counter += 1
        else:
            if counter > SENSITIVITY:
                for j in range(i,len(str_list)):
                    str_list[j] = "0"
                return numerize("".join(str_list))
            counter = 0
    return numerize(result)

while True:
    xaa = numerize(input("enter sqrt: "))
    if xaa == 'cancel':
        break
    print (validate_round(a_root(xaa)))