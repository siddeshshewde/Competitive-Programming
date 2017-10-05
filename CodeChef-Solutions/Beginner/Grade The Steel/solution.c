#include <stdio.h>

int main()
{
	int i, t, hardness, carbon, strength;
	scanf("%d", &t);
	for ( i = 0 ; i < t ; i++)
	{
		scanf("%d%d%d", &hardness, &carbon, &strength);
		if (hardness > 50 && carbon < 0.7 && strength > 5600)
			printf("10\n");
		else
			if (hardness > 50 && carbon < 0.7)
				printf("9\n");
			else 
				if (carbon < 0.7 && strength > 5600)
					printf("8\n");
				else
					if (hardness > 50 &&  strength > 5600)
						printf("7\n");
					else
						if (hardness > 50 || carbon < 0.7 || strength > 5600)
							printf("6\n");
							else
								printf("5\n");
	}
	return 0;
}