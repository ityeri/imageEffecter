# imageEffecter

특징
===

effecsur는 pygame 모듈 기반으로 이미지에 여러 동적 이펙트를 붙일수 있는 간단한 모듈입니다.
현재 시험버전으로 많은 작업을 수동으로 수행해야 합니다.

main_beta.py 는 effecsur 를 이용한 예시 이미지 슬라이드 프로그램입니다.

main_beta.py
===

main_beta.py 는 effecsur 를 이용한 예시 이미지 슬라이드 프로그램입니다.
총 3가지의 예시 동적 이펙트가 있으며 원하는 디렉토르릴 고르면 해당 디렉토리의
모든 이미지 파일을 재귀적으로 불러옵니다.
pyinstaller 로 단일 파일로 패키징 가능합니다.

TODO
===

effecsur:
>   * 다양한 setup 함수 추가
>   * pygame.Surface 의존성 감소
>   * 렌더링 함수 추가

main_beta.py:
>   * UI 추가
>   * 이펙트 추가
