#include <cstdio>
#include <cstring>
#include <cwchar>
#include <windows.h>

int main()
{

	Sleep(2000);

	POINT pt, ptScreen;

	GetCursorPos(&ptScreen);

	pt = ptScreen;

	HWND hParent, hWnd;

	hParent = WindowFromPoint(ptScreen);

	ScreenToClient(hParent, &pt);

	hWnd = ChildWindowFromPoint(hParent, pt);
	wchar_t text[10240], buffer[20240];
	SendMessage(hWnd, WM_GETTEXT, 10240, (LPARAM)text);
//	swprintf(buffer, L"\r\n%ls", text);
//	for(int i = 0; i < 10000; i++)
//	{
//		buffer[i] = text[i];
//	}
	SendMessage(hWnd, WM_SETTEXT, NULL, (LPARAM)buffer);

	return 0;
}
