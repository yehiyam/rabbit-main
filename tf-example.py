import time
import tensorflow

def start(args, hkubeapi):
    input_range=args.get('input')[0]
    # create a variable, refer to it as 'state' and set it to 0
    state = tf.Variable(0)

    # set one to a constant set to 1
    one = tf.constant(1)

    # update phase adds state and one and then assigns to state
    addition = tf.add(state, one)
    update = tf.assign(state, addition )

    # create a session
    with tf.Session() as sess:
    # initialize session variables
    sess.run( tf.global_variables_initializer() )

    print ("The starting state is",sess.run(state))

    print ("Run the update 10 times...")
    for count in range(input_range):
        # execute the update
        sess.run(update)

    print("The end state is",sess.run(state))
    return str(sess.run(state))
