# API Documentation

## View common chord combinations

In order to view common chord combinations, the API can be called using a GET request. The endpoint is http://localhost:5000/common.

A JSON response is returned showing the top 10 most common chord tri-grams found in the data.

## Provide a starting chord to generate a sequence

A starting chord can be submitted in order to generate a sequence of likely chords to follow. This can be done either through the HTML form or by accessing the API with a POST request.

**HTML Form**

The form `web/chord-gram.html` can be used to access a simple User Interface, where the user can enter the starting chord and click the `generate` button to create the sequence.

![](/static/Capture.png)

**API Access**

The API can be called using a POST request. The endpoint is http://localhost:5000/generate.

The header must be set to `"Content-Type: application/json"`

The request body is the starting chord provided as a JSON string. For example:
> "C"


A JSON response is returned showing the generated sequence. For example:


> "C Am/C Bm7 A Em7 C Am A D C"

Note that even if you do not change the starting chord, a new sequence will be generated each time you make the request. The code uses Python weighted random choices, so chords with a higher probability of following the starting chord are more likely to be selected, but there is still a degree of randomness. 