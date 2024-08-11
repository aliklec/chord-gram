

# View common chord combinations

The API can be called using a GET request. The endpoint is http://localhost:5000/common.

A JSON response is returned showing the top 10 most common 3-chord progressions.

# Provide a starting chord to generate a sequence

The API can be called using a POST request. The endpoint is http://localhost:5000/generate.

Make sure to set the header to "Content-Type: application/json"

The request body is the starting chord provided as a JSON string. For example:
> "C"


A JSON response is returned showing the generated sequences. For example:


> "C Am/C Bm7 A Em7 C Am A D C"

Note that even if you do not change the starting chord, a new sequence will be generated each time you make the request. The code uses Python weighted random choices, so chords with a higher probability of following the starting chord are more likely to be selected, but there is still a degree of randomness. 