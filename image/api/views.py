from urllib import response
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import (
    api_view,
    authentication_classes,
    permission_classes,
)
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.pagination import PageNumberPagination
from rest_framework.generics import ListAPIView
from rest_framework.filters import SearchFilter, OrderingFilter

from image.api.serializers import ImageSerializer

from image.api.utilis import remove_bacground_from_image


@api_view(["POST"])
@permission_classes([])
@authentication_classes([])
def api_upload_image(request):  # sourcery skip: avoid-builtin-shadow

    if request.method != "POST":
        return
    serializer = ImageSerializer(data=request.data)

    if serializer.is_valid():
        data = serializer.save()
        try:
            path = data.image.path
            width = data.width
            height = data.height
            remove_bacground_from_image(path, width, height)

            return Response(data={"status": "success", "response": data.image.url})
        except BaseException as e:
            return Response(
                data={
                    "status": "error",
                    "response": str(e),
                },
                status=status.HTTP_400_BAD_REQUEST,
            )
    else:
        print(serializer.errors)
        return Response(
            data={
                "status": "error",
                "response": serializer.errors,
            },
            status=status.HTTP_400_BAD_REQUEST,
        )


# curl -s https://static.remove.bg/remove-bg-web/669d7b10b2296142983fac5a5243789bd1838d00/assets/start_remove-c851bdf8d3127a24e2d137a55b1b427378cd17385b01aec6e59d5d4b5f39d2ec.png | rembg > output.png
