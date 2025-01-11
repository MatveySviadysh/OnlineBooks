from aiohttp import web

@web.middleware
async def error_handler(request, handler):
    try:
        response = await handler(request)
        if response.status == 404:
            return web.json_response({'success': False, 'message': 'The requested resource was not found'}, status=404)
        return response
    except web.HTTPException as ex:
        return web.json_response({'success': False, 'message': str(ex)}, status=ex.status)
    except Exception as e:
        return web.json_response({'success': False, 'message': f'General error: {str(e)}'}, status=500)
