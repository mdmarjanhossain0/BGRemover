from urllib import response
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.pagination import PageNumberPagination
from rest_framework.generics import ListAPIView
from rest_framework.filters import SearchFilter, OrderingFilter

from image.api.serializers import ImageSerializer

from workermodule.djconnetinginterface import cutout

from rembg import remove
import cv2


import os






@api_view(['POST'])
@permission_classes([])
@authentication_classes([])
def api_upload_image(request):

	if request.method == 'POST':
		serializer = ImageSerializer(data=request.data)

		if serializer.is_valid():
			data = serializer.save()
			path=data.image.path




			# try:
				# cutout(path)

			pre, ext = os.path.splitext(path)
			os.rename(path, pre + ".png")
			filename = path.split('/')[-1]
			output_path = "output.png"
			input = cv2.imread(pre + ".png")
			output = remove(input)
			cv2.imwrite(pre + ".png", output)
			# except:
			# 	return Response(data = {
			# 		"status": "error",
			# 		"response": "Some this is wrong. It cann't possible to process"
			# }, status = status.HTTP_400_BAD_REQUEST)
			return Response(data = {
				"status": "success",
				"response": data.image.url
			})
		else:
			print(serializer.errors)
			return Response(data = {
				"status": "error",
				"response": serializer.errors,
			}, status = status.HTTP_400_BAD_REQUEST)



# 			from rembg import remove
# import cv2

# input_path = "test.jpg"
# output_path = 'output.png'

# input = cv2.imread(input_path)
# output = remove(input)
# cv2.imwrite(output_path, output)



# from rembg import remove
# from PIL import Image

# input_path = 'test.jpg'
# output_path = 'output.png'

# input = Image.open(input_path)
# output = remove(input)
# output.save(output_path)


# curl -s https://static.remove.bg/remove-bg-web/669d7b10b2296142983fac5a5243789bd1838d00/assets/start_remove-c851bdf8d3127a24e2d137a55b1b427378cd17385b01aec6e59d5d4b5f39d2ec.png | rembg > output.png